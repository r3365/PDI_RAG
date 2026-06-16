import os
import subprocess
import time
import warnings

import chromadb
import httpx
import gradio as gr

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

CHROMA_DIR = r'F:\OneDrive\Documents\20. AI\PDI_RAG\chroma_db'
COLLECTION_NAME = 'ncc2025'
LM_STUDIO_BASE = 'http://100.115.64.101:1234/v1'
MODEL = 'bartowski/llama-3.2-1b-instruct'
LMS = r'C:\Users\regan\.lmstudio\bin\lms.exe'


def ensure_model_loaded():
    try:
        result = subprocess.run([LMS, 'ls'], capture_output=True, text=True, timeout=10)
        if MODEL in result.stdout:
            print(f"  Model already loaded: {MODEL}")
            return

        print(f"  Loading model: {MODEL} ...")
        subprocess.run([LMS, 'load', MODEL, '-y'], capture_output=True, timeout=120)
        for i in range(30):
            time.sleep(2)
            result = subprocess.run([LMS, 'ls'], capture_output=True, text=True, timeout=10)
            if MODEL in result.stdout:
                print(f"  Model loaded: {MODEL}")
                return
            print(f"    waiting... ({i + 1}/30)")
        print("  Warning: Model may not have loaded in time.")
    except FileNotFoundError:
        print("  Warning: lms CLI not found, skipping auto-load.")
    except Exception as e:
        print(f"  Warning: Could not auto-load model: {e}")


ensure_model_loaded()

client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_collection(COLLECTION_NAME)
print(f"  Loaded vector index: {collection.count()} chunks")
print(f"  Model: {MODEL}")

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

    url = f"{LM_STUDIO_BASE}/chat/completions"
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful building code expert assistant. Use markdown formatting in your responses."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.1,
        "max_tokens": 1024,
        "stream": False,
    }

    try:
        with httpx.Client(timeout=120.0) as c:
            resp = c.post(url, json=payload)
            resp.raise_for_status()
            answer = resp.json()["choices"][0]["message"]["content"]
    except httpx.ConnectError:
        answer = "Error: Cannot connect to LM Studio. Make sure the server is running."
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
