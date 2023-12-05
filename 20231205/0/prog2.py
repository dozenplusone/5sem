import asyncio


async def snd(evsnd: asyncio.Event):
    evsnd.set()
    print(f"snd: generated {evsnd}")


async def mid1(evsnd: asyncio.Event, evmid1: asyncio.Event):
    await evsnd.wait()
    print(f"mid1: received {evsnd}")
    evmid1.set()
    print(f"mid1: generated {evmid1}")


async def mid2(evsnd: asyncio.Event, evmid2: asyncio.Event):
    await evsnd.wait()
    print(f"mid2: received {evsnd}")
    evmid2.set()
    print(f"mid2: generated {evmid2}")


async def rcv(evmid1: asyncio.Event, evmid2: asyncio.Event):
    await asyncio.gather(evmid1.wait(), evmid2.wait())
    print(f"rcv: received {evmid1}")
    print(f"rcv: received {evmid2}")


async def main():
    evsnd, evmid1, evmid2 = [asyncio.Event() for i in range(3)]
    await asyncio.gather(
        snd(evsnd),
        mid1(evsnd, evmid1),
        mid2(evsnd, evmid2),
        rcv(evmid1, evmid2)
    )


asyncio.run(main())
