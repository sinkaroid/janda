import asyncio
from janda import Hentaifox

hentaifox = Hentaifox()

async def get():
    data = await hentaifox.get(59026)
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
