from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser

model = ChatOpenAI(temperature=0)
prompt = ChatPromptTemplate.from_template("generate nodejs code to do following: {problem}")
chain = prompt | model | StrOutputParser()
x = chain.invoke({"problem": "detect pallindrome number"})
print(x)
