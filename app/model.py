from cachetools import TTLCache
from config import model
from langchain_core.prompts import ChatPromptTemplate
from rich import print
from system_prompt import prompt as ai_prompt
from vector import search

chat_memory = TTLCache(maxsize=7, ttl=300)
# chat_memory = []


def add_history(chat):
    chat_memory[chat_memory.currsize + 1] = chat


async def geneate_response(query):
    docs = search(query=query)
    print(docs)
    # add_history(query)
    print(chat_memory)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                ai_prompt,
            ),
            ("human", "{question}"),
        ]
    )

    rag = prompt | model
    async for chunk in rag.astream(
        {"context": docs, "history": chat_memory, "question": query}
    ):
        # print(res.content)
        if chunk:
            yield chunk.content


if __name__ == "__main__":
    geneate_response("What is the eligibility criteria for the scholarship?")
