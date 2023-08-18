import datetime
import utils
import json
import os
from datetime import datetime

# $addbirthday <discordID> <month>/<day>
# $addbirthday @ConnorGoodman 1/8
async def setBirthday(message) :
    await utils.sendMessage(message, "Setting birthday")
    command, args = utils.parseInput(message.content)

    if (not utils.validateLengthOfArgs(args, 2)) :
        await utils.sendMessage(message, "Invalid number of arguments")
        return
    
    userId = args[0]

    if (not utils.isValidDiscordId(userId)) :
        await utils.sendMessage(message, "Invalid discord user")
        return
    
    birthdayString = args[1]

    if (not utils.isValidDateString(birthdayString)) :
        await utils.sendMessage(message, "Invalid date format")
        return
    
    birthdayDateTime = utils.convertDateStringToDateTime(birthdayString)
    
    createUserIfDoesntExist(userId)
    setBirthdayInDatabase(userId, birthdayDateTime)
    await utils.sendMessage(message, "Birthday set")

def createUserIfDoesntExist(userId: str):
    # TODO: check if user exists in the database
    if (not userExistsInDatabase(userId)):
        insertUserIntoDatabase(userId)

def userExistsInDatabase(userId: str) -> bool:
    #TODO: check if user exists in the database

    return userExistsJson(userId)

def setBirthdayInDatabase(userId: str, birthday: datetime):
    # TODO: set birthday in database
    setBirthdayJson(userId, birthday)

def insertUserIntoDatabase(userId: str):
    # TODO: insert user into database
    insertUserJson(userId)

# $getbirthday <discordID>
# $getbirthday @ConnorGoodman
async def getBirthday(message):
    await utils.sendMessage(message, "Getting birthday")
    command, args = utils.parseInput(message.content)

    if (not utils.validateLengthOfArgs(args, 1)) :
        await utils.sendMessage(message, "Invalid number of arguments")
        return
    
    userId = args[0]

    if (not utils.isValidDiscordId(userId)) :
        await utils.sendMessage(message, "Invalid discord user")
        return

    if (not userExistsInDatabase) :
        await utils.sendMessage(message, "User does not exist")
        return
    
    birthdayDateTime = getBirthdayFromDatabase(userId)
    birthdayDateString = utils.convertDateTimeToDateString(birthdayDateTime)

    await utils.sendMessage(message, "Birthday: " + birthdayDateString)

def getBirthdayFromDatabase(userId: str) -> datetime:
    # TODO: get birthday from database
    return getBirthdayJson(userId)

#the json file users.json maps a users id to  their birthday. it looks like this:
# {
#     "id": "birthday"
# }
#this function checks if a user exists in the json file
def userExistsJson(userId: str) -> bool:
    with open('users.json', 'r') as f:
        users = json.load(f)
        if userId in users:
            return True
        else:
            return False
        
#this function sets a users birthday in the json file
def setBirthdayJson(userId: str, birthday: datetime):
    with open('users.json', 'r') as f:
        users = json.load(f)
        users[userId] = birthday.strftime('%m/%d')
    with open('users.json', 'w') as f:
        json.dump(users, f)

#this function inserts a user into the json file
def insertUserJson(userId: str):
    with open('users.json', 'r') as f:
        users = json.load(f)
        users[userId] = ""
    with open('users.json', 'w') as f:
        json.dump(users, f)

#this function gets a users birthday from the json file
def getBirthdayJson(userId: str) -> datetime:
    with open('users.json', 'r') as f:
        users = json.load(f)
        return datetime.strptime(users[userId], '%m/%d')
