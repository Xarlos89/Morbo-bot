from discord.ext import commands

class greet(commands.Cog, command_attrs=dict(hidden=True)):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('Greetings, puny earth-creature.')

	@commands.slash_command()
	async def hello(self, ctx):
	  await ctx.respond(f"Hello, {ctx.author}!")

	@commands.slash_command()
	async def bye(self, ctx):
	  await ctx.respond(f"Bye, {ctx.author}!")


def setup(bot):
	bot.add_cog(greet(bot))
