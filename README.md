# PDI_RAG - NCC2025 Building Code Query Tool

A portable RAG (Retrieval Augmented Generation) pipeline for querying
NCC2025 Australian building code documents and related Australian Standards.

Everything runs **locally on CPU** — no internet, no LM Studio, no cloud API needed.

## Quick Start

1. Install **Python 3.10+** from [python.org](https://python.org)
2. Run the launcher:
   - **Windows**: Double-click `run.bat` or run `.\run.ps1` in PowerShell
3. The launcher creates a venv, installs deps, and starts the local LLM server automatically
4. Select option:
   - `[1]` **Desktop app** — Gradio UI in a Pake/Tauri native window
   - `[2]` **Interactive** — Type questions in the console
   - `[3]` **Single question** — One-off query

## One-liner Query

```powershell
python rag_pipeline.py "What is the minimum clear opening width for an entrance door?"
```

## Stack

| Component | What |
|---|---|
| **PDF to Markdown** | pymupdf4llm |
| **Vector Store** | ChromaDB (persistent, ONNX all-MiniLM-L6-v2, 384-dim) |
| **Generation** | Bundled `llama-server.exe` + Qwen2.5-0.5B-Instruct-Q4_K_M |
| **Desktop UI** | Pake (Tauri/WebView2) wrapping Gradio |
| **Endpoint** | `http://127.0.0.1:8080/v1` (configurable via `LLAMA_ENDPOINT` env var) |

## Files

| File | Description |
|---|---|
| `rag_pipeline.py` | Main RAG script (index, query, interactive) |
| `webapp.py` | Gradio web UI |
| `clean_md.py` | Markdown artifact removal |
| `flag_md.py` / `lint_md.py` | Content quality checks |
| `run.bat` / `run.ps1` | Launcher scripts |
| `md/` | 42 cleaned markdown documents |
| `chroma_db/` | Vector index (11,345 chunks, rebuilt with `python rag_pipeline.py index`) |
| `llama/` | Bundled llama-server runtime + Qwen2.5-0.5B GGUF (not in git, downloaded from LM Studio) |

## Documents Indexed

- NCC2025 Volumes 2 & 3
- Housing Provisions Standard 2025
- Livable Housing Design Standard
- 28 Australian/New Zealand Standards (timber, gas, wiring, plumbing, waterproofing, wind loads, access, pools, etc.)
- 10 ABCB / P&DA Determinations
- NatHERS Technical Note
- AccuRate Materials

**Total: 11,345 chunks across 42 documents.**

## How It Works

1. PDFs are converted to Markdown via `pymupdf4llm`
2. Artifacts stripped by `clean_md.py` (page numbers, headers, boilerplate)
3. Chunked by `##` headings (~500 tokens with overlap)
4. Embedded with ONNX all-MiniLM-L6-v2 and stored in ChromaDB
5. Query: embed question → retrieve top-10 chunks → send to llama-server with context prompt

## Troubleshooting

- **"port already in use"** — Close other apps using port 8080; set `LLAMA_ENDPOINT` for a custom endpoint
- **"No module named..."** — Run `pip install -r requirements.txt`
- **Rebuild index** — `python rag_pipeline.py index` (run after editing `.md` files)
- **Use a remote LLM** — `$env:LLAMA_ENDPOINT = "http://your-server:1234/v1"` then run `python webapp.py`
