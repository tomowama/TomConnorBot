import datetime
import utils

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
    return datetime.datetime.now()
