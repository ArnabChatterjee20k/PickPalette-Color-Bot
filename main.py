import os
from dotenv import load_dotenv
import discord
from discord import Message,GroupChannel
from utils.ai_chat import ai_chat
from utils.livepreview_link import get_livepreview_link
from utils.categorise_palette import categorize_colors
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
    # if client.user in message.mentions:
    #     await message.reply("hey master")
    await message.reply("Building best colors for you...")
    try:
        palettes = ai_chat(message.content)
        categoried_palettes = categorize_colors(palettes)
        live_preview_link = get_livepreview_link(categoried_palettes)
        reply = f"Recommended palettes - {str(palettes)}\nlive preview - {live_preview_link}"
        await message.reply(reply)
    except Exception as e:
        await message.reply("Some problem occured..")
        print(e)
TOKEN = os.environ.get("TOKEN")
client.run(token=TOKEN)