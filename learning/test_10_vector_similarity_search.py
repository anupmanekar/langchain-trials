# Loader - Read Confluence links. Use confluence loader
# Transformer - Create chunks
# Embed - Create Embeddings
# Store - Store embeddings in vector store
# Retrieve

# Create Prompts, to generate bdd scenarios, with embeddings
# Provide jira story number to read data from Jira and provide that as runtime context
import chromadb
from langchain.document_loaders.confluence import ConfluenceLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

loader = ConfluenceLoader(
    url="https://mysite-trial-97.atlassian.net/wiki", username="manekar.anup@gmail.com", api_key=""
)
# documents = loader.load(space_key="~5570588dddbe0b02de4e8088a67297b691e197", page_ids=["425985"], include_attachments=True, limit=50)

documents = loader.load(page_ids=["425985", "425999", "458778", "426022", "589834", "426049"], include_attachments=True, ocr_languages="eng", limit=50)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap  = 20,
    length_function = len,
    add_start_index = True,
)
split_docs = text_splitter.split_documents(documents)

embedding_models = OpenAIEmbeddings()
db = Chroma.from_documents(split_docs, embedding=embedding_models, persist_directory="./chromadb")

""" split_text = []
ids = []
i = 0
for doc in split_docs:
    split_text.append(doc.page_content)
    i = i +1
    ids.append(str(i))
embed_docs = embedding_models.embed_documents(split_text)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="test-10")
collection.add(embeddings=embed_docs, ids=ids) """


query = "What are the age requirements of KYC based registration?"
docs = db.similarity_search(query)

# print results
for doc in docs:
    print(doc.page_content)
