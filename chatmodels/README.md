# Chat Models

Minimal "hello world" examples for the most common LangChain chat-model
providers. Each script loads its API key from the project-root `.env`
via `python-dotenv`, instantiates a chat model, and invokes it with the
single prompt `"What is the capital of France?"`.

## Files

| File | Provider | Model used | Required env var |
| --- | --- | --- | --- |
| `chatmodel_openai.py` | OpenAI (`langchain_openai`) | `gpt-4o-mini` | `OPENAI_API_KEY` |
| `chatmodel_anthropic.py` | Anthropic (`langchain_anthropic`) | `claude-3-5-sonnet-20240620` | `ANTHROPIC_API_KEY` |
| `chatmodel_gemini.py` | Google Generative AI (`langchain_google_genai`) | `gemini-2.5-flash` | `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) |
| `chatmodel_huggingface.py` | Hugging Face (`langchain_huggingface`) | `TinyLlama/TinyLlama-1.1B-Chat-v1.0` via `HuggingFaceEndpoint` | `HUGGINGFACEHUB_API_TOKEN` |

## Chat model vs. LLM

A *chat model* takes a list of role-tagged messages
(`SystemMessage` / `HumanMessage` / `AIMessage`) and returns an
`AIMessage`. A plain *LLM* (see `../llms/`) takes a single string and
returns a string. All modern providers expose chat endpoints, so these
examples use the `Chat*` classes.

## Common parameters

- `temperature` — randomness of the output. `0.0` is deterministic;
  values up to `2.0` are progressively more random.
- `max_completion_tokens` — upper bound on tokens generated in the
  response. Useful to cap cost / latency.

## How to run

From the project root, with the virtualenv activated:

```powershell
python chatmodels/chatmodel_openai.py
python chatmodels/chatmodel_anthropic.py
python chatmodels/chatmodel_gemini.py
python chatmodels/chatmodel_huggingface.py
```

## Hugging Face notes

`HuggingFaceEndpoint` now routes through Hugging Face's Inference
Providers system. Two things you may need to configure explicitly:

1. Pass `huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")`
   on the endpoint if auto-discovery does not pick it up.
2. Pass `provider="hf-inference"` to force HF's own serverless
   inference rather than letting it auto-route to a third-party
   provider (Featherless, Together, etc.) that needs its own key.

Your HF token must also have the **"Make calls to Inference
Providers"** permission enabled at
<https://huggingface.co/settings/tokens>, otherwise you will see a
`403 Forbidden`.
