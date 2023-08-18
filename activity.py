import datetime
import utils
import discord
import os

# Converts a message into a value of points based on recentcy of last word
def getMessageValue(currTime, lastTime):
    deltaTime = abs(lastTime - currTime)
    if deltaTime > 2:
        deltaTime += 0.05
    if deltaTime < timeGap:
        return max(deltaTime / timeGap, 0.01)
    else:
        return 1
    
# go through reconigzed voice channels to give points to users
def getVoiceValue(channels: list[int]):
    # loop over channels and give a point to a user 
    pass
# update points for a user
def givePoints(id:str, points:int):
    pass

# add person to activity tracker
def addActivity(id:str):
    pass



