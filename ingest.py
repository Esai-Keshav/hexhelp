from langchain_core.documents import Document
from config import vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter

# from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

file_path = "./docs/FIRST GRADUATE SCHOLARSHIP INFORMATION.pdf"
print(file_path)
loader = PyPDFLoader(file_path)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=80,
)

# print(len(loader.load_and_split()))
print(len(loader.load_and_split(text_splitter=text_splitter)))
# vector_store.add_texts("Skills python js golang")
# vector_store.add_documents(documents=[Document(page_content="python js golang")])

# vector_store.save_local("./vector_db/")
