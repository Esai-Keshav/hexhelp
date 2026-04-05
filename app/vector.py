from config import vector_db
from langchain.tools import tool

# def to_db():
#     file_path = "./docs/scholarship.pdf"
#     # file_path = "./docs/FIRST GRADUATE SCHOLARSHIP INFORMATION.pdf"
#     # print(file_path)
#     loader = PyPDFLoader(file_path)
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100,
#     )

#     # print(len(loader.load_and_split()))
#     chunks = loader.load_and_split(text_splitter=text_splitter)
#     vector_store.add_documents(chunks)
#     vector_store.save_local("./vector_db/")


@tool
def search(query: str) -> str:
    """
     Use this tool for ANY question related to scholarships.

    This tool retrieves official scholarship information such as:
    - eligibility criteria
    - application process
    - benefits
    - required documents

    ALWAYS use this tool before answering scholarship queries.

    """
    docs = vector_db.similarity_search(query=query, k=5)
    # print(docs)

    # print([doc.page_content for doc in docs])
    return "\n\n".join([doc.page_content for doc in docs])


if __name__ == "__main__":
    # to_db()
    # search()
    print(vector_db.index.ntotal)
