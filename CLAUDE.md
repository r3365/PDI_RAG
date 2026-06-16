# PDI_RAG - NCC2025 Building Code RAG Pipeline

## Overview
RAG pipeline for querying NCC2025 Australian building code documents. Converts PDFs to Markdown via pymupdf4llm, chunks and indexes into ChromaDB, and answers questions via LM Studio.

## Stack
- **PDF to MD**: pymupdf4llm
- **Vector Store**: ChromaDB (persistent, ONNX all-MiniLM-L6-v2, 384-dim)
- **Generation**: LM Studio at `http://100.115.64.101:1234/v1` (qwen/qwen3-vl-4b)

## Usage
```powershell
python rag_pipeline.py "What is the minimum clear opening width for an entrance door?"
python rag_pipeline.py index          # re-index after editing .md files
python rag_pipeline.py                # interactive mode
python webapp.py                      # Gradio web UI at http://127.0.0.1:7860
```

## Key Files
| File | Description |
|---|---|
| `rag_pipeline.py` | Main RAG script (index, query, interactive) |
| `clean_md.py` | Artifact removal from markdown output |
| `webapp.py` | Gradio web UI |
| `md/*.md` | Cleaned markdown documents |
| `chroma_db/` | ChromaDB persistent vector index |

## Documents Indexed
| Document | Pages | Chunks |
|---|---|---|
| NCC2025-Housing-Provisions.pdf | 602 | 1,344 |
| NCC2025-Vol2.pdf | 330 | 1,115 |
| NCC2025-livable-housing-design.pdf | 24 | 58 |
| NCC2025-Vol3.pdf | -- | 1,246 |
| AS1684.2-2010 Timber Frame Construction | -- | 570 |
| AS5601.1-2013 General Gas | -- | 989 |
| AS3000.2007 Wiring Rules | -- | 1,127 |
| AS3500.2-2018 Sanitary Plumbing | -- | 648 |
| AS3500.3-2018 Stormwater | -- | 492 |
| AS3500.4-2018 Heated Water | -- | 355 |
| AS3500.1-2018 Water Services | -- | 374 |
| AS5601.2-2013 LP Gas | -- | 339 |
| AS2870-2011 Res Slabs & Footings | -- | 465 |
| Housing Energy Efficiency Handbook | -- | 310 |
| AS3500.5-2000 Domestic Plumbing | -- | 56 |
| AS1170.1-2002 Barriers | -- | 72 |
| AS1428.1-2009 Access & Mobility | -- | 178 |
| AS1657-1992 Platforms & Walkways | -- | 57 |
| AS1926.1-2012 Pool Safety Barriers | -- | 121 |
| AS2699.1 Wall Ties | -- | 75 |
| AS3727.1-2016 Pavements | -- | 60 |
| AS4055-2012 Wind Loads Housing | -- | 131 |
| AS4509.2-2010 Stand-alone Power | -- | 42 |
| AS4859.1-2002 Thermal Insulation | -- | 140 |
| AS1170.2-2011 Wind Design | -- | 14 |
| AS3500.0-2003 Glossary | -- | 28 |
| AS1720.2-2006 Timber Structures (OCR) | -- | 21 |
| AS3740-2004 Waterproofing (OCR) | -- | 7 |
| AS3700-2018 Masonry | -- | 0 (needs OCR, user declined) |
| NatHERS Technical Note | -- | 92 |
| AccuRate Materials | -- | 51 |
| 6 x ABCB Determinations | -- | 68 |
| 4 x P&DA Determinations | -- | 437 |
| **Total** | **--** | **11,345** |

## Embedding Models
- **Active**: ChromaDB DefaultEmbeddingFunction (all-MiniLM-L6-v2 ONNX, 384-dim, CPU)
- **Available but not wired**: `mxbai-embed-large-v1-f16.gguf` at `F:\ai models\mixedbread-ai\mxbai-embed-large-v1\` (needs CUDA toolkit or CPU-compatible llama-cpp-python build)
- **Available but not wired**: `embeddinggemma-300m-qat-Q4_0.gguf` at `F:\ai models\lmstudio-community\embeddinggemma-300m-qat-GGUF\`

## Pipeline Structure
1. PDF -> Markdown (pymupdf4llm, seconds per doc)
2. Clean artifacts (clean_md.py: remove pics, page nums, headers, clean bold tables)
3. Chunk by ## headings, ~500 tokens with overlap
4. Embed + store in ChromaDB (ONNX, CPU)
5. Query: embed question -> retrieve top-10 chunks -> send to LM Studio with context prompt
