import faiss
from langchain_community.embeddings import Model2vecEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

embeddings = Model2vecEmbeddings("minishlab/potion-base-8M")

embedding_dim = len(embeddings.embed_query("hello world"))
index = faiss.IndexFlatL2(embedding_dim)

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)


vector_db = FAISS.load_local(
    "./vector_db/",
    embeddings,
    allow_dangerous_deserialization=True,
)

model = init_chat_model(
    model="llama-3.1-8b-instant",
    model_provider="groq",
    temperature=0.3,
    max_tokens=250,
)
