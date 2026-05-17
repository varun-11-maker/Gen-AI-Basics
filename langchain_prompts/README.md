# LangChain Prompts

Examples of building and reusing prompts with LangChain — both
free-form chat history and parameterised templates.

## Files

| File | What it demonstrates |
| --- | --- |
| `chatbot.py` | Multi-turn chat loop. Maintains a `chat_history` list of `SystemMessage` / `HumanMessage` / `AIMessage` objects and re-sends the whole history on every turn so the model has context. |
| `chat_prompt_template.py` | `ChatPromptTemplate.from_messages([...])` — a reusable template with placeholders (`{domain}`, `{topic}`) that get filled in at call time. |

## `PromptTemplate` vs. `ChatPromptTemplate`

- `PromptTemplate` — single string template, intended for plain LLMs
  that take one prompt string.
- `ChatPromptTemplate` — a list of role-tagged message templates
  (`system`, `user`, `assistant`), intended for chat models that
  take a list of messages.

Use `ChatPromptTemplate` whenever you target a chat model (which is
almost always today).

## Required environment

Both scripts use Gemini, so add to the project-root `.env`:

```
GEMINI_API_KEY=AIza...
```

## How to run

From the project root, with the virtualenv activated:

```powershell
python langchain_prompts/chat_prompt_template.py

# Interactive chatbot — type messages and press Enter; type "exit" to quit.
python langchain_prompts/chatbot.py
```

## Notes on the chatbot loop

`chatbot.py` checks for `"exit"` *after* appending the user message
but *before* invoking the model, which means the `"exit"` message
ends up in history without a reply. That is fine for a demo, but in
production you would usually break out before appending. The
re-invocation of the full `chat_history` each turn is what gives the
model memory of earlier turns.
