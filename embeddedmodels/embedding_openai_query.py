from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

text = "Hello, how are you?"

embedding = embeddings.embed_query(text)

print(str(embedding))