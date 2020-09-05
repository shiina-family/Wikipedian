from discord.ext import commands
import bs4
import discord
import requests
import urllib

class Function(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def wiki(self, ctx, title: str, location="ja"):
        locations = ["en", "ja"]
        if location not in locations:
            return
        r = requests.get(f"https://{location}.wikipedia.org/wiki/{title}")
        element = bs4.BeautifulSoup(r.text, "html.parser")
        element.find("img").extract()
        if location == "en":
            element.select("p", {"class":"mw-empty-elt"})[0].extract()
            element.select("p", {"class":"mw-empty-elt"})[1].extract()
        e = discord.Embed(title=f"__{element.h1.get_text()}__", description=urllib.parse.unquote(r.url))
        lendesc = len(element.select(".mw-parser-output > p")[0].get_text() + element.select(".mw-parser-output > p")[1].get_text())
        if(lendesc > 280):
            e.set_footer(text=(element.select(".mw-parser-output > p")[0].get_text() + element.select(".mw-parser-output > p")[1].get_text())[:280-(lendesc+1)] + "...")
        else:
            e.set_footer(text=element.select(".mw-parser-output > p")[0].get_text() + element.select(".mw-parser-output > p")[1].get_text())
        # e.set_thumbnail(url=element.find("img")["src"])
        await ctx.send(embed=e)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Function(bot))
