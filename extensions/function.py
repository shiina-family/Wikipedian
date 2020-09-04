import discord
from discord.ext import commands
import launcher
import requests
import bs4
import urllib

class function(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def wiki(self, ctx, title: str):
        r = requests.get("https://ja.wikipedia.org/wiki/"+title)
        element = bs4.BeautifulSoup(r.text)
        e = discord.Embed(title=f"__{element.h1.get_text()}__", description=urllib.parse.unquote(r.url))
        e.set_author(icon_url=ctx.author.avatar_url_as(format="png", size=1024), name=ctx.author)
        e.set_footer(text=element.select(".mw-parser-output > p")[0].get_text())
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(function(bot))