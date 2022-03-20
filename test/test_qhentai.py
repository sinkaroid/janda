import asyncio
from janda import Qhentai

qh = Qhentai()

async def get():
    data = await qh.search("succubus")
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
