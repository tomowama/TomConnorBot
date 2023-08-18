import datetime
import discord
import os
import json
import birthdays
import utils
import activity
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(command_prefix='?', intents=discord.Intents.all())

connect_str = os.getenv('AZURE_BLOB_CONNECTION_STRING')
storage_str = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)



@client.event
async def on_message(message):
    print(message.content)
    command, args = utils.parseInput(message.content)
    if not utils.isValidCommand(command):
        return

    if "$test" == command:
        await message.channel.send("We are online")

    if "$setbirthday" == command:
        await birthdays.setBirthday(message)

    if "$getbirthday" == command:
        await birthdays.getBirthday(message)
        
    if "$track" == command: # strart tracking a user and checks if the message is valid 
        if utils.validateLengthOfArgs(args,1) and utils.isValidDiscordID(args[0]): # ensures there is only one argument, makes sure arg is an valid ID
            if not utils.isTracked(args[0]):
                utils.addActivity(args[0])
                await message.channel.send(f"Started tracking {args[0]}")
            else:
                await message.channel.send(f"Already tracking {args[0]}")
        else:
            await message.channel.send(f"Not a valid arugment. To use properly send: $track @user")
            
        
client.run(os.getenv('DISCORD_TOKEN'))
