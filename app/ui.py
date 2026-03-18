import chainlit as cl
from model import geneate_response


@cl.on_message
async def main(message: cl.Message):
    # ai = geneate_response(message.content)
    # await cl.Message(
    #     content=ai,
    # ).send()

    msg = cl.Message(content="")

    await msg.send()

    async for chunk in geneate_response(message.content):
        await msg.stream_token(chunk)

    await msg.update()
