from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temperature is the randomness of the model
# 0.0 is the most deterministic, 2.0 is the most random
# max_completion_tokens is the maximum number of tokens to generate
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0,max_completion_tokens=100)
message = model.invoke("What is the capital of France?")
print(message)