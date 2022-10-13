from discord.ext import commands

class startup(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Greetings, puny earth-creature.')

def setup(client):
    client.add_cog(startup(client))