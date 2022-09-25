import discord
from discord.ext import commands
import os
import time
from apitest import check_reddit_account


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='r!', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.command()
async def reddit(ctx):
    await ctx.send("https://reddit.com")

boolean=True
while True:
	if boolean:
		if check_reddit_account("TylerHelperFinal")[0]:
			await client.get_channel(837114010301759489).send(check_reddit_account("TylerHelperFinal")[1] + check_reddit_account("TylerHelperFinal")[2] + '<@627917067332485120>')
			boolean=False
	time.sleep(1.5)



client.run(os.getenv("DISCORD_TOKEN"))