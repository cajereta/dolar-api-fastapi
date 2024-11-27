import asyncio
import gc


async def gc_collect():
    while True:
        await asyncio.sleep(3600)
        gc.collect()
