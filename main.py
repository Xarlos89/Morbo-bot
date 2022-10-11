import os
from discord.ext import commands

client = commands.Bot(command_prefix = ">")

if __name__ == "__main__":
	for f in os.listdir("./cogs"):
		if f.endswith(".py")
			client.load_extension("cogs." + f[:-3])

	client.run("token")

