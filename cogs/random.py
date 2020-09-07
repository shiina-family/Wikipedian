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

    @commands.command(aliases=["r"])
    async def random(self, ctx, lang="en"):
        # language
        if lang not in const.langs:
            await ctx.send("That language is not supported.")
            return
        wikipedia.set_lang(lang)
def setup(bot):
    bot.add_cog(Random(bot))
