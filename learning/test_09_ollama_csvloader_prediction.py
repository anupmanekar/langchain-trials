# pip install langchain langchain-experimental openai

from sys import argv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOllama
from langchain.vectorstores import FAISS
from langchain.embeddings.ollama import OllamaEmbeddings
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser


#db = mysql.connector.connect(host="localhost", user="root", password=)
loader = CSVLoader(file_path='/Users/anupmanekar/DevWorkspace/stock-market-data/NIFTY_50_mini_Data.csv', source_column='Date', csv_args={
    'delimiter': ',',
    'quotechar':'"',
    'fieldnames': ['Date', 'Open Points', 'High Points', 'Low Points', 'Close Points']
    })
data = loader.load()

embeddings = OllamaEmbeddings(base_url="http://localhost:11434", model="llama2")
vectorstore = FAISS.from_documents(data, embeddings)
retriever = vectorstore.as_retriever()

template = """Answer based on NIFTY50 stock index data provided in context: {context}: At how much points did NIFTY50 stock index open on {daterange} """

model = ChatOllama(max_tokens=500)
prompt = ChatPromptTemplate.from_template(template=template)

test_generation_chain = (
    {"context": retriever, "daterange": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)

x = test_generation_chain.invoke(input=argv[1])
print(x)