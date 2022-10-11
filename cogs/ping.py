from discord.ext import commands

class startup(commands.Cog):
	def __init__(self, client):
		self.client = client 
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Greetings, puny earth-creature.')
	
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("I see all.")

def setup(client):
	client.add_cog(startup(client))
