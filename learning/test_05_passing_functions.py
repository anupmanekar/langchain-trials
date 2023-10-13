from sys import argv
import json
from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from operator import itemgetter

def length_function(text):
    return len(text)

def _multiple_length_function(text1, text2):
    return len(text1) * len(text2)

def multiple_length_function(_dict):
    return _multiple_length_function(_dict["text1"], _dict["text2"])

prompt = ChatPromptTemplate.from_template("what is {a} + {b}")
model = ChatOpenAI()

chain1 = prompt | model

chain = {
    "a": itemgetter("foo") | RunnableLambda(length_function),
    "b": {"text1": itemgetter("foo"), "text2": itemgetter("bar")} | RunnableLambda(multiple_length_function)
} | prompt | model

x = chain.invoke(json.loads(argv[1]))
print(x)