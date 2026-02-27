from config import vector_store, embeddings, vector_db
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


def to_db():
    file_path = "./docs/FIRST GRADUATE SCHOLARSHIP INFORMATION.pdf"
    print(file_path)
    loader = PyPDFLoader(file_path)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
    )

    # print(len(loader.load_and_split()))
    chunks = loader.load_and_split(text_splitter=text_splitter)
    vector_store.add_documents(chunks)
    vector_store.save_local("./vector_db/")


def search(query="FIRST GRADUATE SCHOLARSHIP INFORMATION ?"):
    docs = vector_db.similarity_search(query=query, k=3)

    print([doc.page_content for doc in docs])
    return [doc.page_content for doc in docs]


if __name__ == "__main__":
    # to_db()
    # search()
    print(vector_db.index.ntotal)
