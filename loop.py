import utils 
import activity
import birthdays
import asyncio


async def everyMinute(client):
    while True:
        print("looping")
        jn = utils.openJSON()
        trackedChannels = list(jn["activity"]["channels"]) # returns dict of channels which are tracked
        print(trackedChannels)
        
        activity.giveVoicePoints(client,trackedChannels)
        await asyncio.sleep(60)