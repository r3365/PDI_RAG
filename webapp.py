import os
from pathlib import Path
import warnings

import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
import httpx
import gradio as gr

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

_SCRIPT_DIR = Path(__file__).parent.resolve()

CHROMA_DIR = str(_SCRIPT_DIR / 'chroma_db')
COLLECTION_NAME = 'ncc2025'
LLAMA_URL = os.getenv('LLAMA_ENDPOINT', 'http://127.0.0.1:8080/v1')


client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(COLLECTION_NAME)
print(f"  Loaded vector index: {collection.count()} chunks")

def build_context(question):
    results = collection.query(query_texts=[question], n_results=10)
    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    context_parts = []
    sources = []
    for doc, meta, dist in zip(chunks, metadatas, distances):
        src = meta.get("source", "?")
        h = meta.get("heading", "")
        score = 1.0 - dist
        sources.append(f"- **{src}** | {h} | relevance: {score:.2f}")
        context_parts.append(f"[{src} / {h}]\n{doc}")

    context_text = "\n\n---\n\n".join(context_parts)
    source_text = "\n".join(sources)
    return context_text, source_text

def ask(question, history):
    context_text, source_text = build_context(question)

    prompt = (
        "You are a building code expert assistant. Answer the question based "
        "only on the provided context from the National Construction Code 2025 "
        "documents. If the context doesn't contain enough information, say so. "
        "Quote relevant section numbers when applicable.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {question}\nAnswer:"
    )

    url = f"{LLAMA_URL}/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful building code expert assistant. Use markdown formatting in your responses."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.1,
        "max_tokens": 1024,
    }

    try:
        with httpx.Client(timeout=120.0) as c:
            resp = c.post(url, json=payload)
            resp.raise_for_status()
            answer = resp.json()["choices"][0]["message"]["content"]
    except httpx.ConnectError:
        answer = "Error: Cannot connect to LLM server. Make sure the backend is running."
    except httpx.HTTPStatusError as e:
        detail = ""
        try:
            detail = e.response.text[:500]
        except Exception:
            pass
        answer = f"Error: LLM server returned HTTP {e.response.status_code}. {detail}"
    except Exception as e:
        answer = f"Error: {e}"

    sources_formatted = f"\n\n**Sources:**\n{source_text}"
    return answer + sources_formatted

with gr.Blocks(
    title="NCC2025 Building Code Q&A",
    theme=gr.themes.Soft(),
    fill_height=True,
    css=".gradio-container { max-width: 100% !important; }"
) as demo:
    gr.Markdown(
        "# NCC2025 Building Code Q&A\n"
        "Ask questions about the National Construction Code 2025 "
        "(Housing Provisions, Volume Two, Livable Housing Design)"
    )

    chatbot = gr.ChatInterface(
        fn=ask,
        chatbot=gr.Chatbot(height="70vh", min_height=400),
        title=None,
        description=None,
        fill_width=True,
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
