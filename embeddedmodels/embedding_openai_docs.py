from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

documents = ["Hello, how are you?",
    "I am fine, thank you."
    ]

embeddings = embeddings.embed_documents(documents)

print(str(embeddings))