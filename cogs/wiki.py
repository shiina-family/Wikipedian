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

        # search
        response = wikipedia.search(keyword)
        if not response:
            await ctx.send("Wikipedia not found.")
            return
        try:
            page = wikipedia.page(response[0])
        except wikipedia.exceptions.DisambiguationError as e:
            await ctx.send("Please clear up that keyword ambiguity.")
            return
        except Exception as e:
            await ctx.send("Unexpected error occurred.")
            return

        # embed
        embed = discord.Embed(
            title=page.title,
            url=urllib.parse.unquote(page.url),
            description=page.content[0:200].replace("\n", " ") + "..."
        )
        embed.set_thumbnail(url=page.images[0])
        embed.set_footer(
            text="You can go to Wikipedia by clicking on the title.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
