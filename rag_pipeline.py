#!/usr/bin/env python3

import os
import sys
import re
import warnings
import argparse
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
import httpx


warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'


MD_DIR = r'F:\OneDrive\Documents\20. AI\PDI_RAG\md'
CHROMA_DIR = r'F:\OneDrive\Documents\20. AI\PDI_RAG\chroma_db'
COLLECTION_NAME = 'ncc2025'
LM_STUDIO_BASE = 'http://100.115.64.101:1234/v1'

TOKEN_BUDGET = 500
TOKEN_OVERLAP = 50
CHARS_PER_TOKEN = 4


def estimate_tokens(text):
    return max(1, len(text) // CHARS_PER_TOKEN)


def get_sections(content):
    lines = content.split('\n')
    sections = []
    current_heading = "Preamble"
    current_lines = []

    for line in lines:
        if re.match(r'^## ', line):
            if current_lines:
                text = '\n'.join(current_lines).strip()
                if text:
                    sections.append((current_heading, text))
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        text = '\n'.join(current_lines).strip()
        if text:
            sections.append((current_heading, text))

    return sections


def chunk_section(heading, text, source_file):
    paragraphs = re.split(r'\n\n+', text)
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    chunks = []
    current_paras = []
    current_tokens = 0

    def flush():
        nonlocal current_paras, current_tokens
        if not current_paras:
            return
        chunk_text = '\n\n'.join(current_paras)
        chunks.append((source_file, heading, chunk_text))

        overlap_paras = []
        overlap_tokens = 0
        for p in reversed(current_paras):
            pt = estimate_tokens(p)
            if overlap_tokens + pt > TOKEN_OVERLAP and overlap_paras:
                break
            overlap_paras.insert(0, p)
            overlap_tokens += pt
        current_paras = list(overlap_paras)
        current_tokens = overlap_tokens

    for para in paragraphs:
        para_tokens = estimate_tokens(para)

        if para_tokens >= TOKEN_BUDGET:
            flush()
            words = para.split()
            sub_chunk = []
            sub_tokens = 0
            for word in words:
                wt = estimate_tokens(word + ' ')
                if sub_tokens + wt > TOKEN_BUDGET and sub_chunk:
                    chunks.append((source_file, heading, ' '.join(sub_chunk)))

                    overlap_words = []
                    overlap_tok = 0
                    for w in reversed(sub_chunk):
                        wt2 = estimate_tokens(w + ' ')
                        if overlap_tok + wt2 > TOKEN_OVERLAP and overlap_words:
                            break
                        overlap_words.insert(0, w)
                        overlap_tok += wt2
                    sub_chunk = list(overlap_words)
                    sub_tokens = overlap_tok

                sub_chunk.append(word)
                sub_tokens += wt

            if sub_chunk:
                chunks.append((source_file, heading, ' '.join(sub_chunk)))
            continue

        if current_tokens + para_tokens > TOKEN_BUDGET and current_paras:
            flush()

        current_paras.append(para)
        current_tokens += para_tokens

    flush()
    return chunks


def chunk_markdown_files():
    md_files = sorted(Path(MD_DIR).glob('*.md'))
    if not md_files:
        print("  No .md files found in md/ directory.")
        sys.exit(1)

    all_chunks = []
    for md_path in md_files:
        content = md_path.read_text(encoding='utf-8')
        sections = get_sections(content)
        file_chunks = []
        for heading, text in sections:
            section_chunks = chunk_section(heading, text, md_path.name)
            file_chunks.extend(section_chunks)
        all_chunks.extend(file_chunks)
        print(f"  {md_path.name}: {len(file_chunks)} chunks from {len(sections)} sections")

    print(f"  Total: {len(all_chunks)} chunks across {len(md_files)} files")
    return all_chunks


def build_index(client):
    print("Building NCC2025 vector index...")
    chunks = chunk_markdown_files()

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=DefaultEmbeddingFunction(),
    )

    print("  Adding chunks to vector store...")
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        ids = [f"chunk_{j}" for j in range(i, i + len(batch))]
        documents = [text for _, _, text in batch]
        metadatas = [{"source": src, "heading": h} for src, h, _ in batch]
        collection.add(documents=documents, ids=ids, metadatas=metadatas)
        end = min(i + batch_size, len(chunks))
        print(f"    Indexed chunks {i + 1}–{end} / {len(chunks)}")

    print("  Indexing complete.")
    return collection


def get_collection(client):
    try:
        collection = client.get_collection(COLLECTION_NAME)
        if collection.count() > 0:
            return collection
    except ValueError:
        pass
    return None


def ensure_index(client):
    collection = get_collection(client)
    if collection is not None:
        print(f"  Found existing index with {collection.count()} chunks.")
        return collection
    return build_index(client)


def get_lm_studio_model():
    try:
        with httpx.Client(timeout=5.0) as c:
            resp = c.get(f"{LM_STUDIO_BASE}/models")
            resp.raise_for_status()
            models = resp.json().get("data", [])
            if models:
                return models[0]["id"]
    except Exception:
        pass
    return None


def query_lm_studio(messages, model=None):
    url = f"{LM_STUDIO_BASE}/chat/completions"
    payload = {
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 1024,
        "stream": False,
    }
    if model:
        payload["model"] = model

    try:
        with httpx.Client(timeout=120.0) as c:
            resp = c.post(url, json=payload)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
    except httpx.ConnectError:
        print(f"\nError: Cannot connect to LM Studio at {LM_STUDIO_BASE}")
        print("Make sure LM Studio server is running with API enabled.")
        sys.exit(1)
    except httpx.HTTPStatusError as e:
        print(f"\nError: LM Studio returned HTTP {e.response.status_code}")
        print(f"Response: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"\nError querying LM Studio: {e}")
        return None


def answer_question(question, collection, model):
    results = collection.query(
        query_texts=[question],
        n_results=10,
    )

    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    print("\n" + "=" * 70)
    print("RETRIEVED CONTEXT:")
    print("=" * 70)
    for i, (doc, meta, dist) in enumerate(zip(chunks, metadatas, distances)):
        score = 1.0 - dist
        src = meta.get("source", "?")
        heading = meta.get("heading", "")
        preview = doc[:120].replace('\n', ' ').strip()
        print(f"\n  [{i + 1}] Score: {score:.4f} | {src} | {heading}")
        print(f"      {preview}...")

    context_parts = []
    for d, m in zip(chunks, metadatas):
        src = m.get("source", "?")
        h = m.get("heading", "")
        context_parts.append(f"[{src} / {h}]\n{d}")
    context_text = "\n\n---\n\n".join(context_parts)

    prompt = (
        "You are a building code expert assistant. Answer the question based "
        "only on the provided context from the National Construction Code 2025 "
        "documents. If the context doesn't contain enough information, say so. "
        "Quote relevant section numbers when applicable.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {question}\nAnswer:"
    )

    answer = query_lm_studio([
        {"role": "system", "content": "You are a helpful building code expert assistant."},
        {"role": "user", "content": prompt},
    ], model=model)

    print("\n" + "=" * 70)
    print("ANSWER:")
    print("=" * 70)
    print(answer)
    return answer


def main():
    parser = argparse.ArgumentParser(description="NCC2025 RAG Pipeline")
    parser.add_argument("query", nargs="?", default=None,
                        help="Question to ask, or 'index' to rebuild")
    args = parser.parse_args()

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    if args.query == "index":
        build_index(client)
        return

    collection = ensure_index(client)
    model = get_lm_studio_model()
    if model:
        print(f"  LM Studio model: {model}")
    else:
        print("  LM Studio: using loaded model (name not detected)")

    if args.query:
        answer_question(args.query, collection, model)
    else:
        print()
        print("NCC2025 RAG Pipeline - Interactive Mode")
        print("Type 'quit', 'exit', or 'q' to exit.")
        while True:
            try:
                question = input("\nQuestion: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            if not question:
                continue
            if question.lower() in ('quit', 'exit', 'q'):
                break

            answer_question(question, collection, model)


if __name__ == '__main__':
    main()
