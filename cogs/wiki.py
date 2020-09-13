import const
import discord
import wikipedia
from discord.ext import commands
from urllib.parse import unquote


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["w"])
    async def wiki(self, ctx, lang, *, keywords):
        # language
        if lang not in const.langs:
            await ctx.send("That language is not supported.")
            return
        wikipedia.set_lang(lang)

        # search
        response = wikipedia.search(keywords, results=1)
        if not response:
            await ctx.send("Wikipedia not found.")
            return
        try:
            page = wikipedia.page(response)
        except wikipedia.exceptions.DisambiguationError:
            await ctx.send("Please clear up that keywords ambiguity.")
            return
        except Exception:
            await ctx.send("Unexpected error occurred.")
            return

        # embed
        cont = page.content.replace("\n", " ")

        title = page.title
        url = unquote(page.url)
        description = cont if len(cont) <= 200 else cont[:200] + "..."
        thumbnail = next((image for image in page.images if not image.endswith(".svg")),
                         "https://cdn.discordapp.com/attachments/752286472383758416/752286652042313739/no_image.png")
        text = "Tips: You can go to Wikipedia by clicking the title."

        embed = discord.Embed(title=title, url=url, description=description)
        embed.set_thumbnail(url=thumbnail)
        embed.set_footer(text=text)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))
