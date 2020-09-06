import urllib

import bs4
import discord
import requests
from discord.ext import commands


class Others(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")


def setup(bot):
    bot.add_cog(Others(bot))
