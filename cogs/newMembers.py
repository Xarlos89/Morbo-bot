import discord
from discord.ext import commands

class newMember(commands.Cog, command_attrs=dict(hidden=True)):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		if channel is not None:
			# The Introductions channel.
			await bot.get_channel(int(953543179133665380)).send(f'Welcome {member.mention}.')

def setup(bot):
	bot.add_cog(newMember(bot))
