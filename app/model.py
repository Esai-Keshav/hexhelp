from config import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from rich import print
from system_prompt import prompt as ai_prompt
from vector import search
from langchain.agents import create_agent


state = {"messages": []}


async def geneate_response(query):
    state["messages"].append({"role": "user", "content": query})
    state["messages"] = state["messages"][-6:]

    ai_msg = ""
    rag = create_agent(model=model, tools=[search], system_prompt=ai_prompt)

    async for chunk in rag.astream(state):
        print(chunk)  # debug

        if "model" in chunk:
            messages = chunk["model"].get("messages", [])
            if messages:
                content = messages[-1].content
                if content:
                    ai_msg += content
                    # state["messages"].append({"role": "assistant", "content": ai_msg})
                    yield content


if __name__ == "__main__":
    geneate_response("What is the eligibility criteria for the scholarship?")
