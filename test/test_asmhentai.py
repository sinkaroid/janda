import asyncio
from janda import Asmhentai

asm = Asmhentai()

async def get():
    data = await asm.get(311851)
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
