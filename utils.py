import discord
import os
from datetime import datetime

# function that parses the input of a discord command and outputs a dictionary
# of the command and the arguments
def parseInput(input: str) -> dict:
    input = input.split(" ")
    return input

def convertDateToDateTime(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d')