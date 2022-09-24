#this is a test
import discord
import os
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix="r!", intents = intents)
client.remove_command("help")

load_dotenv()


@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")
	await client.change_precense(activity = discord.Activity(
		type = discord.ActivityType.watching,
		name = "Reddit posts." )
	)

@client.command(pass_context = True)
async def on_message(message):
	if message.startsWith("r!reddit"):
		await ctx.send("reddit.com")

client.run(os.getenv("DISCORD_TOKEN"))
