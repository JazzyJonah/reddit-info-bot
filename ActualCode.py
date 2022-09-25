import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command
async def reddit(ctx):
	ctx.send("https://reddit.com")

client.run(os.getenv("DISCORD_TOKEN"))  