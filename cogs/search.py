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
        # language
        if lang not in const.langs:
            await ctx.send("That language is not supported.")
            return
        wikipedia.set_lang(lang)

        # search
        response = wikipedia.search(keyword)
        if not response:
            await ctx.send("Wikipedia not found.")
            return
        try:
            tmp = wikipedia.page(response[0])
        except wikipedia.exceptions.DisambiguationError as e:
            await ctx.send("Please clear up that keyword ambiguity.")
            return
        except Exception as e:
            await ctx.send("Unexpected error occurred.")
            return

        # embed
        value = ""
        for temp in response:
            page = wikipedia.page(temp)
            value += f"[{page.title}]({urllib.parse.unquote(page.url)})\n"
        embed = discord.Embed(title="Search Result")
        embed.add_field(
            name=f"Top {len(response)} searches.",
            value=value
        )
        embed.set_footer(
            text="You can go to Wikipedia by clicking on the title.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Search(bot))
