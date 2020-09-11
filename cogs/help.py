from textwrap import dedent
from discord.ext import commands

class Help(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send(dedent("""\
            **Wikipedian** allows you to search wikipedia in a better way.

            > `/wiki <language code> <keywords>`
            Search a article that contains `keywords` from Wikipedia and send message with an embed.

            > `/search <language code> <keywords>`
            Search for articles on Wikipedia by `keywords` and send them as a list with an embed.

            > `/random (<language code>)`
            Randomly send a article from Wikipedia.

            See also GitHub for more information:
            https://github.com/mii-group/Wikipedian
            """))


def setup(bot):
    bot.add_cog(Help(bot))
