import discord
from discord.ext import commands
import wikipedia
import urllib
import const


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["s"])
    async def search(self, ctx, lang, *, keyword):


def setup(bot):
    bot.add_cog(Search(bot))
