import asyncio
from janda import Thentai

thentai = Thentai()

async def get():
    data = await thentai.get(608979)
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
