from vector import search
from langchain_core.prompts import ChatPromptTemplate
from config import model


def geneate_response(query):
    docs = search(query=query)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that helps answer questions based on the following context: {context}",
            ),
            ("human", "{question}"),
        ]
    )

    rag = prompt | model
    res = rag.invoke({"context": docs, "question": query})
    print(res.content)


if __name__ == "__main__":
    geneate_response("What is the eligibility criteria for the scholarship?")
