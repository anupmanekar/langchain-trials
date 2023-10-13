from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI


llm = OpenAI()
a = llm.predict("Behave as computer engineer and use geeky terms and tell me which food you like", temperature=0)
chat_model = ChatOpenAI()
x = chat_model.predict("Behave as banker and tell me which food you like", temperature=0)
print (a)
print ("----------------")
print (x)