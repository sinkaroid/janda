import asyncio
from janda import Nhentai

nhentai = Nhentai()

async def get():
    data = await nhentai.get(255369)
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
