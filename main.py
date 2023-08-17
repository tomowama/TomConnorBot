import datetime
import discord
import os
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(command_prefix='?', intents=discord.Intents.all())

###################################################
################# BLOB STUFF ######################
###################################################
connect_str = os.getenv('AZURE_BLOB_CONNECTION_STRING')
storage_str = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

filesToGet = [] # files that will be pulled from the blob on inital startup

def getBlobs(files: list[str]): #retrieves content of files from the blob

    for fileName in files:
        blob_client = blob_service_client.get_blob_client(
            container=storage_str, blob=fileName)
        
        with open(fileName, "wb") as my_blob:
            stream = blob_client.download_blob()
            data = stream.readall()
            my_blob.write(data)

def writeToBlob(fileName: str):  # write local changes of a file to the blob
    blob_client = blob_service_client.get_blob_client(container=storage_str, blob=fileName)

    with open(fileName, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

###################################################
################# BLOB STUFF ######################
###################################################



###################################################
################ COMMANDS #########################
###################################################

@client.event
async def on_message(message):
    if "$test" in message.content.lower():
        await message.channel.send("We are online")

    if '$addbirthday' in message.content.lower():
        await addBirthday(message)

###################################################
################ COMMANDS #########################
###################################################




###################################################
################ FUNCTIONS ########################
###################################################

# $addbirthday <name> <month>/<day>
# $addbirthday Connor Goodman 1/8
async def addBirthday(message) :
    input = parseInput(message.content)
    month = input[1]
    day = int(input[2])

    birthdays = getAllBirthdays()
    foundBday = checkIfBirthdayExists(birthdays)

    if (not foundBday):
        insertBirthday()

    f = open("birthdays.json", "w")
    json.dump(birthdays, f)
    f.close()

def convertDateToDateTime(date: str) -> datetime:
    return datetime.strptime(date, '%m/%d')

def getAllBirthdays() -> list[dict]:
    f = open("birthdays.json", "r")
    birthdays = json.load(f)
    f.close()
    return birthdays

def checkIfBirthdayExists(birthdays) -> bool:
    for x in birthdays:
        if (x['name'].lower() == name.lower()):
            x['day'] = day
            x['month'] = month
            message.channel.send('Changed birthday!')

def insertBirthday() :
    dict = {'name': name, 'day': day, 'month': month}
    birthdays.append(dict)
    f = open("birthdays.json", "w")
    json.dump(birthdays, f)
    f.close()
    message.channel.send('Added birthday!')
    
    
###################################################
################ FUNCTIONS ########################
###################################################


client.run(os.getenv('DISCORD_TOKEN'))
