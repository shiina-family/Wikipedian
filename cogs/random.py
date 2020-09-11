import asyncio
import discord
from discord.ext import commands
import wikipedia
import urllib
import const
from concurrent import futures


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def searcher(self):
        try:
            title = wikipedia.random()
            result = wikipedia.search(title, results=1)
            return wikipedia.page(result)
        except Exception:
            return self.searcher()

    async def searcher_async(self):
        with futures.ThreadPoolExecutor() as executor:
            fut = executor.submit(self.searcher)
            return await asyncio.wrap_future(fut)

    @commands.command(aliases=["r"])
    async def random(self, ctx, lang="en"):
        # language
        if lang not in const.langs:
            await ctx.send("That language is not supported.")
            return
        wikipedia.set_lang(lang)

        # search
        page = await self.searcher_async()
        if page.title == "Main Page":
            await ctx.send("Oops. I have gotten nothing Wikipedia.\n"
                           "Maybe the Wikipedia for that language is closed.\n"
                           f"Do you wanna check?: <{page.url}>")
            return

        # embed
        cont = page.content.replace("\n", " ")

        title = page.title
        url = urllib.parse.unquote(page.url)
        description = cont if len(cont) <= 200 else cont[:200] + "..."
        thumbnail = next((image for image in page.images if not image.endswith(".svg")),
                         "https://cdn.discordapp.com/attachments/752286472383758416/752286652042313739/no_image.png")
        text = "Tips: You can also specify the language code as an argument."

        embed = discord.Embed(title=title, url=url, description=description)
        embed.set_thumbnail(url=thumbnail)
        embed.set_footer(text=text)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Random(bot))
