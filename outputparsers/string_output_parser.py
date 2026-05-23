from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# this open source model does not support structured output so we use output parsers to convert it into structured output
llm = HuggingFaceEndpoint(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = "Write a detailed report on the topic {topic}",
    input_variables = ["topic"]
)

template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text:\n {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

