import datetime
import discord
import os
import json
import birthdays
import utils
import activity
import loop 
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(command_prefix='?', intents=discord.Intents.all())

connect_str = os.getenv('AZURE_BLOB_CONNECTION_STRING')
storage_str = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)



@client.event
async def on_ready(): # runs on startup 
    client.loop.create_task(loop.everyMinute(client))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.content)
    command, args = utils.parseInput(message.content)
    authorID = utils.toStrID(message.author.id) # gives message author id in <@123123> format
    if not utils.isValidCommand(command):
        return

    elif "$test" == command:
        await message.channel.send("We are online")
    elif args == None:
        await message.channel.send("Not a valid command, or no arugments")
    elif "$setbirthday" == command:
        await birthdays.setBirthday(message)

    elif "$getbirthday" == command:
        await birthdays.getBirthday(message)
        
    elif "$track" == command: # strart tracking a user and checks if the message is valid 
        if not utils.isValidDiscordIDSingle(args): # ensures there is only one argument, makes sure arg is an valid ID
            await message.channel.send("Invalid use of command. Use like: $track @user")
        elif activity.track(args):
            await message.channel.send(f"Started Tracking {args[0]}")
        else:
            await message.channel.send(f"Already Tracking {args[0]}")
            
        
client.run(os.getenv('DISCORD_TOKEN'))
