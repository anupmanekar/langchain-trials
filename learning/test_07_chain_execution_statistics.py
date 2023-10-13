from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.callbacks import get_openai_callback


model = ChatOpenAI(temperature=0)
prompt = ChatPromptTemplate.from_template("generate nodejs code to do following: {problem}")
chain = prompt | model | StrOutputParser()

with get_openai_callback() as cb:
    x = chain.invoke({"problem": "detect pallindrome number"})
    print(cb)
    print(x)
