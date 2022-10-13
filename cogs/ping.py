from discord.ext import commands

class extra(commands.Cog):
	def __init__(self, client):
		self.client = client 
	
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("I see all.")

def setup(client):
	client.add_cog(extra(client))
