import discord
from discord.ext import commands
import wikipedia
import urllib
import const


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Random(bot))
