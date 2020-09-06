import urllib

import bs4
import discord
from discord.ext import commands
import wikipedia
import urllib
import const


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["w"])
    async def wiki(self, ctx, lang, *, keyword):
        # language
        if lang not in const.langs:
            await ctx.send("That language is not supported.")
            return
        wikipedia.set_lang(lang)

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
        if ctx.invoked_subcommand is None:
            await ctx.send("このコマンドには言語指定が必要です。例: /wiki ja イデア論")

    @wiki.command()
    async def ja(self, ctx, *, keyword):
        r = requests.get(f"https://ja.wikipedia.org/wiki/{keyword}")
        element = bs4.BeautifulSoup(r.text, "html.parser")
        element.find("img").extract()
        await self.scrape_wiki(ctx, element, r)

    @wiki.command()
    async def en(self, ctx, *, keyword):
        r = requests.get(f"https://en.wikipedia.org/wiki/{keyword}")
        element = bs4.BeautifulSoup(r.text, "html.parser")
        element.find("img").extract()
        element.select("p", {"class": "mw-empty-elt"})[0].extract()
        element.select("p", {"class": "mw-empty-elt"})[1].extract()
        await self.scrape_wiki(ctx, element, r)

def setup(bot):
    bot.add_cog(Wiki(bot))
