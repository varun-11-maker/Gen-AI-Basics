from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0.0,max_completion_tokens=100)
message = model.invoke("What is the capital of France?")
print(message)