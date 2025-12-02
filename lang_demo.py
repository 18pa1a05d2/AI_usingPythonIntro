# we also have promptTemplate, but for applications we use ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = ChatPromptTemplate.from_template("{input}")
llm = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = prompt | llm | parser

while True:
    value = input("you: ")
    if value.lower() in ["exit", "quit"]:
        break
    chain = prompt | llm | parser
#Runnable -> perform invoke only on runnable objects
    answer = chain.invoke({"input":value})
    print("AI : "+answer)
