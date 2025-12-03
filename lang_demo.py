# we also have promptTemplate, but for applications we use ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import MessagesPlaceholder
load_dotenv()

prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder("history"),"{input}"])
llm = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = prompt | llm | parser

store = {}
session_id="maha_lakshmi_1"

def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id]= ChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

while True:
    value = input("you: ")
    if value.lower() in ["exit", "quit"]:
        break
    
#Runnable -> perform invoke only on runnable objects
    answer = chain_with_history.invoke({"input":value},config={"configurable": {"session_id":session_id}})
    print("AI : "+answer)
