import discord
import os
from datetime import datetime

# function that parses the input of a discord command and outputs a dictionary
# of the command and the arguments
def parseInput(input: str) -> dict:
    input = input.split(" ")
    command = input[0]
    args = input[1:]
    input = {"command": command, "args": args}
    return input

def convertDateToDateTime(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d')

def isValidDiscordId(discordId: str) -> bool:
    return (discordId[0] == "<" and discordId[1] == "@" and discordId[-1] == ">")

def sendMessage(message, text) :
    message.channel.send(text)