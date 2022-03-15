import asyncio
from janda import Hentai2read

h2r = Hentai2read()

async def get():
    data = await h2r.get("jeanne_alter_wants_to_mana_transfer")
    print(data)

async def main():
    await asyncio.gather(get())

asyncio.run(main())
