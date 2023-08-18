import datetime
import utils
import discord
import os

TIMEGAP = 60 # ammount of time for full point messages in minutes

# update points for a user, assumes user is being tracked
def givePoints(id:str, points:int):
    jn = utils.openJSON()
    jn["activity"]["user"][id]["points"] += points
    print(jn["activity"]["user"][id]["points"])
    utils.writeJSON(jn)


# Converts a message into a value of points based on recentcy of last word
def getMessageValue(currTime, lastTime):
    deltaTime = abs(lastTime - currTime)
    if deltaTime < TIMEGAP:
        return max(deltaTime / TIMEGAP, 0.01)
    else:
        return 1

def giveMessagePoints(id:str):
    if not utils.isTracked(id):
        return
    # need to get last time they send message for JSON
    lastTime = utils.getLastMessageTime(id)
    currTime = utils.convertDateTimeToInt()
    points = getMessageValue(currTime,lastTime)
    utils.updateLastMessageTime(id,currTime)
    givePoints(id,points)
  
# go through reconigzed voice channels to give points to users will be run every minute
def giveVoicePoints(channels: list[int]):
    # loop over channels and give a point to a user 
    # give 0.025 points per minute
    for channelNum in channels:
        channel = main.client.get_channel(channelNum)
        if len(channel.members > 1):
            for mem in channel.members:
                memID = utils.toStrID(mem.id)
                if utils.isTracked(memID):
                    givePoints(memID,0.025)

    

def genWeeklyLeaderboard() -> list[list[str]]:
    pass

def genAllTimeLeaderboard() -> list[list[str]]:
    pass


    

