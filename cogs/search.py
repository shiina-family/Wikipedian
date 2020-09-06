import discord
from discord.ext import commands
import wikipedia
import urllib
import const


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def search(self, ctx, *, keyword):
        r = requests.get(
            f"https://ja.wikipedia.org/wiki/Special:Search?search={keyword}&go=Go&ns0=1")
        element = bs4.BeautifulSoup(r.text, "html.parser")
        results = []
        check = []
        c = element.find(".mw-parser-output > p")
        check.append(c)
        for result in element.select(".mw-search-result-heading"):
            results.append("・" + result.get_text())
        if results:
            e=discord.Embed(title="Search Result",
                            description="\n".join(results[:15]))
            e.set_footer(
                text=f"Total: {len(results)}(showing 15 of total items)")
        else:
            if check:
                e = discord.Embed(
                    title="Search Result",
                    description="Page found.\n"+urllib.parse.unquote(r.url))
            else:
                e = discord.Embed(
                    title="Search Result",
                    description="result not found.")
                e.set_footer(text="Total: 0")
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Search(bot))
