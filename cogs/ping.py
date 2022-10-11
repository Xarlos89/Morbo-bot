from discord.ext import commands

class ping(commands.Cog):
	def __init__(self, client):
		self.client = client 
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Up and running.')
	
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("I see all.")

def setup(client):
	client.add_cog(ping(client))