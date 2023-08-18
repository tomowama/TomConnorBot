from datetime import datetime
import json

############################# Input/Output ###########################################

def parseInput(input: str) -> dict:
    input = input.split(" ")
    command = input[0].lower()
    args = input[1:]
    return command, args

async def sendMessage(message, text) :
    await message.channel.send(text)

def toStrID(id:int) -> str:
    return f"<@{id}>"

############################# Input/Output ###########################################

############################# DateTime ###########################################


def convertDateStringToDateTime(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d')

def convertDateTimeToDateString(date: datetime) -> str:
    return date.strftime('%m/%d')

# converts a the current time to a int to compare to other times to tell amount of time difference 
def convertDateTimeToInt() -> int:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ll = current_time.split(":")
    time = 0
    for i in range(3):
        if i == 0:
            time += int(ll[0]) * 60
        elif i == 1:
            time += int(ll[1])
        else:
            time += int(ll[2]) / 60
    return time

############################# DateTime ###########################################

############################# Validation ###########################################

def isValidDiscordId(discordId: str) -> bool:
    return (discordId[0] == "<" and discordId[1] == "@" and discordId[-1] == ">")

def isValidCommand(command: str) -> bool:
    return (command[0] == "$")

def validateLengthOfArgs(args: list, length: int) -> bool:
    return len(args) == length

def isValidDateString(date: str) -> bool:
    try:
        datetime.strptime(date, '%m/%d')
        return True
    except ValueError:
        return False

############################# Validation ###########################################

############################# JSON ###########################################


# opens JSON
def openJSON() -> dict:
    f = open('users.json','r+')
    users = json.load(f)
    f.close()
    return users

#writes a dict to a JSON
def writeJSON(dic):
    f = open('users.json','r+')
    json.dump(dic, f)
    f.close()

# checks if user is being tracked
def isTracked(id:str) -> bool:
    jn = openJSON()
    if id not in jn["activity"]["user"]:
        return False
    return True
#Assumes user is being tracked
def getLastMessageTime(id:str) -> int:
    jn = openJSON()
    return jn["activity"]["user"][id]["lastMsg"]
    
def updateLastMessageTime(id:str,time:int):
    jn = openJSON()
    jn["activity"]["user"][id]["lastMsg"] = time
    writeJSON(jn)
        
# add person to activity tracker
def addActivity(id:str):
    if not isTracked:
        jn = openJSON()
        jn["activity"]["user"][id] = {"points": 0, "lastMsg": 0}
        writeJSON(jn)
    
############################# JSON ###########################################