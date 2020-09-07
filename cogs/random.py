import discord
from discord.ext import commands
import wikipedia
import urllib
import const


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def seacher(self):
        try:
            title = wikipedia.random()
            results = wikipedia.search(title)
            return wikipedia.page(results[0])
        except Exception:
            print(results)
            return self.seacher()

def setup(bot):
    bot.add_cog(Random(bot))
