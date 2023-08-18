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

###################################################
################# BLOB STUFF ######################
###################################################



###################################################
################ COMMANDS #########################
###################################################

@client.event
async def on_message(message):
    print(message.content)
    userInput = utils.parseInput(message.content)
    if "$test" == userInput.command.lower():
        await message.channel.send("We are online")

    if "$setbirthday" == userInput.lower():
        await birthdays.setBirthday(message)

###################################################
################ COMMANDS #########################
###################################################



client.run(os.getenv('DISCORD_TOKEN'))
