from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model
print ("Input Schema:")
print (chain.input_schema.schema())
print ("Output Schema:")
print (chain.output_schema.schema())
