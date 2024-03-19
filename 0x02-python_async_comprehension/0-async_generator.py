import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = random.randint(0, 10)
        yield random_number  # Step 5: Yield the random number

