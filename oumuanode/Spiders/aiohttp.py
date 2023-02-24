import asyncio
import aiohttp

urls = [
    "https://img-baofun.zhhainiao.com/market/133/2d64f9b1d09b9c519b301d4d721adc0c.jpg",
    "https://img-baofun.zhhainiao.com/market/133/f43477adecc82e51dd1f5bd901c854c5_preview_raw.jpg"
]


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())


async def main():
    tasks = []
    for url in urls:
        d = asyncio.create_task(aiodownload(url))
        tasks.append(d)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
