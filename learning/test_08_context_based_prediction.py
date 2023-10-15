# pip install langchain openai faiss-cpu tiktoken
from sys import argv
from operator import itemgetter

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import FAISS

# Define retriever, in other words context.
vectorstore = FAISS.from_texts(["SSO login is available only for premium customers and not free subscribers.", 
                                "Free subscribers can only use normal authentication", "All users have to set 2FA authentication",
                                "Setting 2FA auth is available after first login which user cannot skip",
                                "User can update from being free subscriber by paying a premium of 5 USD"], embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

template = """Generate all test scenarios and steps for use cases based only on the following context:
{context}

Use Case: {usecase}
"""

model = ChatOpenAI(max_tokens=4000)
prompt = ChatPromptTemplate.from_template(template=template)

test_generation_chain = (
    {"context": retriever, "usecase": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)

x = test_generation_chain.invoke(input=argv[1])
print(x)