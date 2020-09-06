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

        try:
            p0txt = element.select(".mw-parser-output > p")[0].get_text()
        except:
            p0txt = "Page not found."
        try:
            p1txt = element.select(".mw-parser-output > p")[1].get_text()
        except:
            p1txt = ""

        lendesc = len(p0txt + p1txt)
        if(lendesc > 280):
            e.set_footer(text=(p0txt + p1txt)[:280-(lendesc+1)] + "...")
        else:
            e.set_footer(text=p0txt + p1txt)

        await ctx.send(embed=e)

    @commands.command()
    async def search(self, ctx, *, keyword):
        r = requests.get("https://ja.wikipedia.org/wiki/Special:Search?search="+keyword)
        element = bs4.BeautifulSoup(r.text, "html.parser")
        results = []
        crowed = 0
        for result in element.select(".mw-search-result-heading > a"):
            results.append(result)
            print()
            crowed+=1
            if(crowed > 10):
                break
        e=discord.Embed(title="Search Result", description=[r.get_text()+":"+urllib.parse.unquote(r["href"]) for r in results])
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Function(bot))
