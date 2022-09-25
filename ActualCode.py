import discord
from discord.ext import commands
import os
import time


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='r!', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.command()
async def reddit(ctx):
    await ctx.send("https://reddit.com")



client.run(os.getenv("DISCORD_TOKEN"))