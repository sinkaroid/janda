import asyncio
from janda import Pururin

pururin = Pururin()

async def get():
    data = await pururin.get(47226)
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
