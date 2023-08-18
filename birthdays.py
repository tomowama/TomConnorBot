import datetime
import utils
import discord
import os

# $addbirthday <discordID> <month>/<day>
# $addbirthday @ConnorGoodman 1/8
async def setBirthday(message) :
    input = utils.parseInput(message.content)
    userId = input[1]
    birthdayString = input[2]
    birthdayDateTime = utils.convertDateToDateTime(birthdayString)
    createUserIfDoesntExist(userId)

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

