#this is a test
import discord
from discord.ext import commands

intents = Intents.default()
intents.members = True

client = commands.Bot(command_prefix="r!")
client.remove_command("help")


@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")
	await client.change_precense(activity = discord.Activity(
		type = discord.ActivityType.watching,
		name = "Reddit posts." )
	)

@client.command(pass_context = True)
async def reddit():
	await ctx.send("reddit.com")

client.run(str(secrets.discordOathKey))
