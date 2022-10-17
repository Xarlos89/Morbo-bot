import os
import discord
from discord.ext import commands

bot = commands.Bot()

if __name__ == "__main__":

	bot.load_extension('cogs.greetings')
	bot.run("TOKEN")

