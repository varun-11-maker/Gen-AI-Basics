# python_langchain

A hands-on tour of the core building blocks of [LangChain](https://python.langchain.com/),
organised as one folder per concept. Every script is small, self-contained,
and runnable on its own — pick a topic, open the folder, read its README,
and run the file.

## Repository layout

| Folder | Topic | Open the README |
| --- | --- | --- |
| [`chatmodels/`](./chatmodels/README.md) | Chat-style models from OpenAI, Anthropic, Gemini, and Hugging Face. | [README](./chatmodels/README.md) |
| [`llms/`](./llms/README.md) | The legacy completion-style LLM interface (`OpenAI` vs. `ChatOpenAI`). | [README](./llms/README.md) |
| [`embeddedmodels/`](./embeddedmodels/README.md) | Turning text into vector embeddings with `OpenAIEmbeddings` (`embed_query` vs. `embed_documents`). | [README](./embeddedmodels/README.md) |
| [`langchain_prompts/`](./langchain_prompts/README.md) | Multi-turn chat history and reusable `ChatPromptTemplate`s. | [README](./langchain_prompts/README.md) |
| [`structured_output/`](./structured_output/Readme.md) | Forcing model output to a schema via `with_structured_output` — TypedDict, Pydantic, and raw JSON Schema variants. | [Readme](./structured_output/Readme.md) |

## Suggested learning order

1. `chatmodels/` — get a model talking.
2. `llms/` — see what the older completion API looks like and why chat models are now preferred.
3. `langchain_prompts/` — wrap your prompts in reusable templates and add chat history.
4. `structured_output/` — make the model return parseable data instead of prose.
5. `embeddedmodels/` — generate vectors, the foundation for semantic search and RAG.

## Setup

### 1. Create and activate a virtualenv

From the project root, in PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

`requirements.txt` is a full freeze of the working environment. It
pulls in the four LangChain provider integrations
(`langchain-openai`, `langchain-anthropic`, `langchain-google-genai`,
`langchain-huggingface`), `python-dotenv`, `pydantic`, and their
transitive deps.

### 3. Create a `.env` file at the project root

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...
HUGGINGFACEHUB_API_TOKEN=hf_...
```

Notes:

- The Hugging Face variable **must** be named `HUGGINGFACEHUB_API_TOKEN`
  (not `..._API_KEY`); `langchain_huggingface` auto-reads only the
  former.
- Every script calls `load_dotenv()` near the top, so the same `.env`
  is reused everywhere — no per-folder config needed.
- Add `.env` to `.gitignore` if you intend to push this repo anywhere.

## Running an example

Always run from the **project root** (so relative imports and
`load_dotenv()` find the right files):

```powershell
python chatmodels/chatmodel_openai.py
python embeddedmodels/embedding_openai_query.py
python langchain_prompts/chat_prompt_template.py
python structured_output/structured_output_pydantic.py
python llms/llm_demo.py
```

## Provider-specific gotchas

- **Hugging Face** — `HuggingFaceEndpoint` now routes through HF's
  Inference Providers system. If you see
  `ValueError: You must provide an api_key to work with <provider> API`,
  pass `huggingfacehub_api_token=...` and `provider="hf-inference"`
  explicitly, and make sure your HF token has the **"Make calls to
  Inference Providers"** permission at
  <https://huggingface.co/settings/tokens>.
- **OpenAI completion-style `OpenAI` class** — works with chat-tuned
  models like `gpt-4o-mini`, but prefer `ChatOpenAI` for any real work.
- **Embeddings** — use the same method (`embed_query` or
  `embed_documents`) on both sides of a similarity comparison; they
  may use slightly different internal prompts.

## Requirements

- Python 3.10+ (tested with the Python that ships in `venv/`).
- Network access for the provider APIs.
- API keys for the providers you want to try (see `.env` above).
- A Hugging Face account with an Inference-Providers-enabled token if
  you want to run `chatmodel_huggingface.py`.
