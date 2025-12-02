# we also have promptTemplate, but for applications we use ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = ChatPromptTemplate.from_template("tell me a joke about {subject}")
llm = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
#chain = prompt | llm
chain = prompt | llm | parser
#Runnable -> perform invoke only on runnable objects
answer = chain.invoke({"subject":"software"})
print(answer)
#print(answer.content)
