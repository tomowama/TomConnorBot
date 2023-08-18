import datetime
import utils
import discord
import os

# $addbirthday <discordID> <month>/<day>
# $addbirthday @ConnorGoodman 1/8
async def setBirthday(message) :
    utils.sendMessage(message, "Setting birthday")
    command, args = utils.parseInput(message.content)
    userId = args[0]
    birthdayString = args[1]
    birthdayDateTime = utils.convertDateToDateTime(birthdayString)
    if (not isValidBirthday(birthdayDateTime)) :
        utils.sendMessage(message, "Invalid birthday")
        return
    
    createUserIfDoesntExist(userId)
    setBirthdayInDatabase(userId, birthdayDateTime)

def isValidBirthday(birthday: datetime) -> bool:
    return birthday < datetime.datetime.now()

def createUserIfDoesntExist(userId: str):
    # TODO: check if user exists in the database
    if (not userExistsInDatabase(userId)):
        insertUserIntoDatabase(userId)

def userExistsInDatabase(userId: str) -> bool:
    #TODO: check if user exists in the database
    return True

def setBirthdayInDatabase(userId: str, birthday: datetime):
    # TODO: set birthday in database
    return

def insertUserIntoDatabase(userId: str):
    # TODO: insert user into database
    return

# $getbirthday <discordID>
# $getbirthday @ConnorGoodman
async def getBirthday(message):
    utils.sendMessage(message, "Getting birthday")
    command, args = utils.parseInput(message.content)
    userId = args[0]

    if (not userExistsInDatabase) :
        utils.sendMessage(message, "User does not exist")
        return
    
    birthdayDateTime = getBirthdayFromDatabase(userId)
    birthdayDateString = utils.convertDateTimeToDateString(birthdayDateTime)

    utils.sendMessage(message, birthdayDateString)

def getBirthdayFromDatabase(userId: str) -> datetime:
    # TODO: get birthday from database
    return datetime.datetime.now()
