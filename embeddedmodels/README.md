# Embedding Models

Small examples that turn text into dense vector embeddings using
OpenAI's embedding API through `langchain_openai`. Embeddings are the
foundation for semantic search, RAG, clustering, and similarity
scoring.

## Files

| File | What it shows |
| --- | --- |
| `embedding_openai_query.py` | Embeds a single string with `embed_query` — the call you use for a user search query. |
| `embedding_openai_docs.py` | Embeds a list of strings with `embed_documents` — the call you use to index a corpus. |

Both scripts use the model `text-embedding-3-large` (3072-dimensional
output). Substitute `text-embedding-3-small` (1536-dim) for a cheaper /
faster alternative.

## `embed_query` vs. `embed_documents`

- `embed_query(text: str) -> list[float]` — produces a single vector.
  Use this at search time.
- `embed_documents(texts: list[str]) -> list[list[float]]` — produces
  one vector per input. Use this at index time.

The two methods may apply slightly different prompts internally
(provider-dependent), so always use the matching method on each side
of a similarity comparison.

## Required environment

Add to the project-root `.env`:

```
OPENAI_API_KEY=sk-...
```

## How to run

From the project root, with the virtualenv activated:

```powershell
python embeddedmodels/embedding_openai_query.py
python embeddedmodels/embedding_openai_docs.py
```

The output is a (very long) Python list of floats — that is the
embedding vector. In a real application you would store these in a
vector database (Chroma, FAISS, Pinecone, Redis, pgvector, etc.) and
query by cosine similarity.
