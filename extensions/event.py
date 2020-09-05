from discord.ext import commands
import bot
import discord


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

    @commands.Cog.listener()
    async def on_ready(self):
        USERNAME = self.bot.user.name
        DISCRIMINATOR = self.bot.user.discriminator
        FULLNAME = str(USERNAME + "#" + DISCRIMINATOR)
        print("logged in as:", FULLNAME, self.bot.user.id)
        game = discord.Game(name=USERNAME + " | Use /wiki <title>")
        await self.bot.change_presence(activity=game)

def setup(bot):
    bot.add_cog(Event(bot))
