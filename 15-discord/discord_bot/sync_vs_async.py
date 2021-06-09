import time
import asyncio

async def do_discord():
    print("Starting discord")
    await asyncio.sleep(4)
    print("Done discord")

async def do_minecraft():
    print("Starting minecraft")
    await asyncio.sleep(3)
    print("Done minecraft")

async def do_english():
    print("Starting english")
    await asyncio.sleep(1)
    print("Done english")


async def do_research():
    await asyncio.gather(do_discord(), do_minecraft(), do_english())

def measure_time():
    start = time.time()

    asyncio.run(do_research())
    end = time.time()

    print("Time taken is ", end - start)

if __name__ == '__main__':
    measure_time()
