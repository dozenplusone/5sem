import asyncio


async def squarer(x):
    return x * x


async def doubler(x):
    return x + x


async def main(*args):
    ans = await asyncio.gather(*(squarer(arg) for arg in args))
    ans = await asyncio.gather(*(doubler(arg) for arg in ans))
    print(*ans)


asyncio.run(main(*eval(input())))
