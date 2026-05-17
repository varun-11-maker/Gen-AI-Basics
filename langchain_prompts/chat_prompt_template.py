from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a {domain} expert."),
    ("user", "Explain in simple terms what is {topic}"),
])

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "The history of cricket"
})

print(prompt)

# prompt_template is used for creating single messages
# chat_prompt_template is used for creating multiple messages