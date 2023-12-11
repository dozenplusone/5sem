import asyncio


ev = asyncio.Event()


async def writer(queue: asyncio.Queue, delay: float):
    cur = 0
    while not ev.is_set():
        await asyncio.sleep(delay)
        await queue.put(f"{cur}_{delay}")
        cur += 1


async def stacker(queue: asyncio.Queue, stack: asyncio.Queue):
    while not ev.is_set():
        await stack.put(await queue.get())


async def reader(stack: asyncio.Queue, count: int, delay: float):
    for i in range(count):
        await asyncio.sleep(delay)
        print(await stack.get())
    ev.set()


async def main():
    queue, stack = asyncio.Queue(), asyncio.Queue()
    delay_w1, delay_w2, delay_r, count = eval(input())
    await asyncio.gather(
        writer(queue, delay_w1),
        writer(queue, delay_w2),
        stacker(queue, stack),
        reader(stack, count, delay_r)
    )


asyncio.run(main())
