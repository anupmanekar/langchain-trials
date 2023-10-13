from sys import argv
import json
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain.schema import StrOutputParser


model = ChatOpenAI()
lunch_chain = ChatPromptTemplate.from_template("give me vegeterian recipe about {lunch}") | model | StrOutputParser()
dinner_chain = ChatPromptTemplate.from_template("give me vegan recipe about {lunch}") | model
draw_chain = ChatPromptTemplate.from_template("draw image of {lunch}") | model

new_lunch_chain = lunch_chain.with_config({"callbacks": get_openai_callback})
map_chain = RunnableParallel(lunch=new_lunch_chain, dinner=dinner_chain, image=draw_chain)

# x = map_chain.invoke({"lunch": "samosa"})
x = map_chain.invoke(json.loads(argv[1]))
print(x)
""" print(x["lunch"])
print("-----------------")
print(x["dinner"])
print("-----------------")
print(x["image"]) """

