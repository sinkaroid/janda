import asyncio
from janda import Thentai, resolve

ge = Thentai()

async def get():
    data = await ge.search("mother")
    print(resolve(data))

async def main():
    await asyncio.gather(get())

asyncio.run(main())
