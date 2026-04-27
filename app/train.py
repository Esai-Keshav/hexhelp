from config import vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


def to_db():
    file_path = "./docs/scholarship.pdf"
    # file_path = "./docs/FIRST GRADUATE SCHOLARSHIP INFORMATION.pdf"
    # print(file_path)
    loader = PyPDFLoader(file_path)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=180,
    )

    # print(len(loader.load_and_split()))
    chunks = loader.load_and_split(text_splitter=text_splitter)
    # print(chunks[:4])
    vector_store.add_documents(chunks)
    vector_store.save_local("./vector_db/")


if __name__ == "__main__":
    to_db()
