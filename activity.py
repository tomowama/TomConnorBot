import datetime
import utils
import discord
import os

TIMEGAP = 60 # ammount of time for full point messages in minutes


def track(args: list[str]) -> bool: # tracks user and checks if they are tracked and if message is valid
    if not utils.isTracked(args[0]):
        utils.addActivity(args[0])
        return True
    else:
        return False
    
            

# update points for a user, assumes user is being tracked
def givePoints(id:str, points:int):
    jn = utils.openJSON()
    jn["activity"]["user"][id]["points"] += points
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
def giveVoicePoints(client, channels: list[str]):
    # loop over channels and give a point to a user 
    # give 0.025 points per minute
    for channelNum in channels:
        channel = client.get_channel(int(channelNum)) # THIS DOESN'T WORK BECASUE OF CIRCULAR IMPORT 
        if len(channel.members )>0:
            for mem in channel.members:
                memID = utils.toStrID(mem.id)
                if utils.isTracked(memID):
                    givePoints(memID,0.025)

    

def genWeeklyLeaderboard() -> list[list[str]]:
    pass

def genAllTimeLeaderboard() -> list[list[str]]:
    pass


    

