import urllib

import bs4
import discord
import requests
from discord.ext import commands


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def scrape_wiki(self, ctx, location):
        r = requests.get(f"https://{location}.wikipedia.org/wiki/{title}")
        element = bs4.BeautifulSoup(r.text, "html.parser")
        element.find("img").extract()
        if location == "en":
            element.select("p", {"class": "mw-empty-elt"})[0].extract()
            element.select("p", {"class": "mw-empty-elt"})[1].extract()
        e = discord.Embed(
            title=f"__{element.h1.get_text()}__",
            description=urllib.parse.unquote(
                r.url))

        try:
            p0txt = element.select(".mw-parser-output > p")[0].get_text()
        except BaseException:
            p0txt = "Page not found."
        try:
            p1txt = element.select(".mw-parser-output > p")[1].get_text()
        except BaseException:
            p1txt = ""

        lendesc = len(p0txt + p1txt)
        if(lendesc > 280):
            e.set_footer(text=(p0txt + p1txt)[:280 - (lendesc + 1)] + "...")
        else:
            e.set_footer(text=p0txt + p1txt)

        await ctx.send(embed=e)

    @commands.group()
    async def wiki(self, ctx):

    @wiki.command()
    async def ja(self, ctx, *, keyword):
        scrape_wiki(ctx, "ja")

    @wiki.command()
    async def en(self, ctx, *, keyword):
        scrape_wiki(ctx, "en")

def setup(bot):
    bot.add_cog(Wiki(bot))
