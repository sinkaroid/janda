import asyncio
from janda import SimplyHentai

sh = SimplyHentai()

async def get():
    data = await sh.get("fate-grand-order/perros")
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
