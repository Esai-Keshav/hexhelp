import chainlit as cl
from model import geneate_response


@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")

    await msg.send()

    async for chunk in geneate_response(message.content):
        await msg.stream_token(chunk)

    await msg.update()
