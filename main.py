import datetime
import discord
import os
import json
import birthdays
import utils
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
        await birthdays.addBirthday(message)

###################################################
################ COMMANDS #########################
###################################################




###################################################
################ FUNCTIONS ########################
###################################################



###################################################
################ FUNCTIONS ########################
###################################################


client.run(os.getenv('DISCORD_TOKEN'))
