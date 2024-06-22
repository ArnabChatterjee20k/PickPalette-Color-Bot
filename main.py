import os
from dotenv import load_dotenv
import discord
from discord import Message,GroupChannel

load_dotenv(".env")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message:Message):
    if message.author == client.user:
        return
    if client.user in message.mentions:
        await message.reply("hey master")
TOKEN = os.environ.get("TOKEN")
client.run(token=TOKEN)