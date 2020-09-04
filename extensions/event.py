import discord
from discord.ext import commands
import launcher

class event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

    @commands.Cog.listener()
    async def on_ready(self):
        USERNAME      = self.bot.user.name
        CLIENT_ID     = self.bot.user.id
        DISCRIMINATOR = self.bot.user.discriminator
        FULLNAME      = str(USERNAME + "#" + DISCRIMINATOR)

        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print(FULLNAME + " is ready({}v).".format(launcher.VERSION))
        game = discord.Game(name=USERNAME + " " + launcher.VERSION + " | Prefix: " + launcher.PREFIX)
        await self.bot.change_presence(activity=game)

def setup(bot):
    bot.add_cog(event(bot))