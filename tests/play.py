import asyncio

loop = asyncio.new_event_loop()
import time

def raiser():
    time.sleep(8)
    raise Exception('ciao')

async def coro():
    await loop.run_in_executor(None, raiser)

t = loop.create_task(coro())
loop.run_until_complete(t)
