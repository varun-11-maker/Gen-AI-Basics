# LLMs (Completion-style Models)

Demonstrates LangChain's *plain LLM* interface — string in, string
out — as opposed to the chat-message interface used in `../chatmodels/`.

## Files

| File | What it shows |
| --- | --- |
| `llm_demo.py` | Loads `OpenAI(model="gpt-4o-mini")` from `langchain_openai`, calls `invoke("What is the capital of France?")`, and prints the response string. |

## LLM vs. Chat model

| | LLM (`langchain_openai.OpenAI`) | Chat model (`langchain_openai.ChatOpenAI`) |
| --- | --- | --- |
| Input | a single `str` | a list of `BaseMessage` objects (system / human / ai) |
| Output | a `str` | an `AIMessage` |
| Use case | Legacy completion endpoints, simple one-shot prompts | Modern multi-turn conversations, tool calling, structured output |

For new code you should almost always prefer the chat interface — see
`../chatmodels/chatmodel_openai.py`. This folder exists to show what
the older completion-style API looks like.

## Required environment

Add to the project-root `.env`:

```
OPENAI_API_KEY=sk-...
```

## How to run

From the project root, with the virtualenv activated:

```powershell
python llms/llm_demo.py
```

## Note about `gpt-4o-mini`

`gpt-4o-mini` is a chat-tuned model. Calling it through the
completion-style `OpenAI` class works because LangChain transparently
adapts the request, but the natural fit for chat-tuned models is
`ChatOpenAI`. For a true completion-style model you would pick one of
the legacy `text-*` or `gpt-3.5-turbo-instruct` models.
