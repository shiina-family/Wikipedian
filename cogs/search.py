from urllib.parse import unquote

import discord
import wikipedia
from discord.ext import commands

import const


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["s"])
    async def search(self, ctx, lang, *, keywords):
        # language
        if lang not in const.langs:
            await ctx.send("That language is not supported.")
            return
        wikipedia.set_lang(lang)

        # search
        response = wikipedia.search(keywords)
        if not response:
            await ctx.send("Wikipedia not found.")
            return
        try:
            tmp = wikipedia.page(response[0])
        except wikipedia.exceptions.DisambiguationError:
            await ctx.send("Please clear up that keywords ambiguity.")
            return
        except Exception:
            await ctx.send("Unexpected error occurred.")
            return

        # embed
        title = "Search Result"
        name = f"Top {len(response)} searches."
        value = ""
        for temp in response:
            page = wikipedia.page(temp)
            value += f"[{page.title}]({unquote(page.url)})\n"
        text = "Tips: You can go to Wikipedia by clicking the title."

        embed = discord.Embed(title=title)
        embed.add_field(name=name, value=value)
        embed.set_footer(text=text)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Search(bot))
