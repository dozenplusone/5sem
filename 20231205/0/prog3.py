import asyncio


async def prod(q1: asyncio.Queue, stop=None):
    for i in range(5):
        await q1.put(p := f"value_{i}")
        print(f"prod: put {p} to q1")
        await asyncio.sleep(1)
    await q1.put(stop)
    print(f"prod: put {stop} to q1")



async def mid(q1: asyncio.Queue, q2: asyncio.Queue, stop=None):
    while True:
        m = await q1.get()
        print(f"mid: got {m} from q1")
        await q2.put(m)
        print(f"mid: put {m} to q2")
        if m == stop:
            break


async def cons(q2: asyncio.Queue, stop=None):
    while True:
        c = await q2.get()
        print(f"cons: got {c} from q2")
        if c == stop:
            break


async def main():
    q1, q2 = asyncio.Queue(), asyncio.Queue()
    await asyncio.gather(
        prod(q1),
        mid(q1, q2),
        cons(q2)
    )


asyncio.run(main())
