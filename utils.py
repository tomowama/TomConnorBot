from datetime import datetime

# function that parses the input of a discord command and outputs a dictionary
# of the command and the arguments
def parseInput(input: str) -> dict:
    input = input.split(" ")
    command = input[0]
    args = input[1:]
    return command, args

def convertDateStringToDateTime(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d')

def convertDateTimeToDateString(date: datetime) -> str:
    return date.strftime('%m/%d')

def isValidDiscordId(discordId: str) -> bool:
    return (discordId[0] == "<" and discordId[1] == "@" and discordId[-1] == ">")

def isValidCommand(command: str) -> bool:
    return (command[0] == "$")

def validateLengthOfArgs(args: list, length: int) -> bool:
    return len(args) == length

async def sendMessage(message, text) :
    await message.channel.send(text)