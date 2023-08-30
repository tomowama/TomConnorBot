import datetime
import discord
import os
import json
import birthdays
import utils
import activity
import loop
from dotenv import load_dotenv
from azure.data.tables import TableServiceClient

load_dotenv()

client = discord.Client(command_prefix='?', intents=discord.Intents.all())

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
storage_str = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
users_table_name = os.getenv('USERS_TABLE_NAME')
globla_data_table_name = os.getenv('GLOBAL_DATA_TABLE_NAME')
timezone = os.getenv('TIMEZONE')

table_service_client = TableServiceClient.from_connection_string(connect_str)
global_data_client = table_service_client.get_table_client(globla_data_table_name)
users_client = table_service_client.get_table_client(users_table_name)

@client.event
async def on_ready(): # runs on startup 
    client.loop.create_task(loop.everyMinute())
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.content)
    command, args = utils.parseInput(message.content)
    authorID = utils.toStrID(message.author.id) # gives message author id in <@123123> format
    if not utils.isValidCommand(command):
        return

    if "$test" == command:
        await message.channel.send("We are online")

    if "$setbirthday" == command:
        await birthdays.setBirthday(message)

    if "$getbirthday" == command:
        await birthdays.getBirthday(message)
        
    if "$track" == command: # strart tracking a user and checks if the message is valid 
        if not utils.isValidDiscordIDSingle(args): # ensures there is only one argument, makes sure arg is an valid ID
            await message.channel.send("Invalid use of command. Use like: $track @user")
        elif activity.track(args):
            await message.channel.send(f"Started Tracking {args[0]}")
        else:
            await message.channel.send(f"Already Tracking {args[0]}")
            
        
client.run(os.getenv('DISCORD_TOKEN'))
