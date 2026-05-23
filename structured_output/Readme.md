# Structured Output

Examples of forcing an LLM to return data that conforms to a defined
schema, using LangChain's `model.with_structured_output(schema)`.
This is the standard way to get reliable, parseable output for
downstream code instead of free-form prose.

> Some open-source models cannot natively produce structured output.
> For those, LangChain falls back to output parsers that prompt the
> model to emit JSON and validate it after the fact. The
> `with_structured_output(...)` helper works for both kinds of
> models — providers that support native function/tool calling
> (OpenAI, Anthropic, Gemini, ...) and those that do not.

## Files

| File | Schema style | What it shows |
| --- | --- | --- |
| `structured_output_typed_dict.py` | `TypedDict` + `Annotated[..., "description"]` | Lightest-weight option. Field descriptions come from `Annotated` metadata. Result is a plain `dict`. |
| `structured_output_pydantic.py` | `pydantic.BaseModel` | Full validation, defaults, and `Field(description=...)`. Result is a typed model instance. Preferred for anything non-trivial. |
| `structured_output_json_schema.py` | Raw JSON Schema `dict` | Useful when the schema is defined externally (e.g. loaded from a `.json` file) or shared with non-Python consumers. Result is a plain `dict`. |
| `pydantic_refresher.py` | — | Standalone refresher on Pydantic itself: defining a `BaseModel`, validators, `Field` constraints (`gt`, `lt`, `default`), `EmailStr`, and `model_dump_json()`. Not a LangChain example. |
| `json_schema.json` | — | Tiny example JSON Schema document, kept for reference. |

All three structured-output scripts use the same input: a Samsung
Galaxy S24 Ultra review. They extract `key_themes`, `summary`,
`sentiment` (`"pos"` / `"neg"`), `pros`, `cons`, and `name`.

## Choosing a schema style

- **`TypedDict`** — quickest to write; pick when you only need shape,
  not validation.
- **`pydantic.BaseModel`** — pick when you need defaults, optional
  fields with sensible behaviour, or want to use the result as a
  typed object downstream. This is the recommended default.
- **JSON Schema dict** — pick when the schema is the source of truth
  outside Python (e.g. shared with a frontend or another service).

## Required environment

All three scripts use Gemini, so add to the project-root `.env`:

```
GEMINI_API_KEY=AIza...
```

## How to run

From the project root, with the virtualenv activated:

```powershell
python structured_output/structured_output_typed_dict.py
python structured_output/structured_output_pydantic.py
python structured_output/structured_output_json_schema.py
```

Each script prints the parsed result — a `dict` for the TypedDict and
JSON-Schema variants, a `Review` instance for the Pydantic variant.
