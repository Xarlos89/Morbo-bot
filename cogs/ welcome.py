from discord.ext import commands

class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            print(f'Welcome {member.mention}.')
            # await channel.send(f'Welcome {member.mention}.')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            print(f'Hello {member.name}~')
            # await ctx.send(f'Hello {member.name}~')
        else:
            print(f'Hello {member.name}... This feels familiar.')
            # await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

def setup(client):
    client.add_cog(welcome(client))
