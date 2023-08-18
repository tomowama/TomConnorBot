import utils 
import activity
import birthdays
import asyncio


async def everyMinute():
    while True:
        print("looping")
        
        await asyncio.sleep(60)