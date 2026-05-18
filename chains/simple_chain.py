from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "What is the capital of {country}",
    input_variables = ["country"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chain = prompt | model | parser

result = chain.invoke({'country':'France'})
print(result)

chain.get_graph().print_ascii()
