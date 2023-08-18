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

connect_str = os.getenv('AZURE_BLOB_CONNECTION_STRING')
storage_str = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

@client.event
async def on_message(message):
    print(message.content)
    command, args = utils.parseInput(message.content)
    if not utils.isValidCommand(command):
        return

    if "$test" == command.lower():
        await message.channel.send("We are online")

    if "$setbirthday" == command.lower():
        await birthdays.setBirthday(message)

client.run(os.getenv('DISCORD_TOKEN'))
