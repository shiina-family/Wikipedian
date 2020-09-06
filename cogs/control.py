from discord.ext import commands


class Control(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, cog):
        self.bot.load_extension("cogs." + cog)
        await ctx.send(f"Loaded Extension: {cog}.py")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, cog):
        if cog == "control":
            await ctx.send("You can't unload it!")
        self.bot.unload_extension("cogs." + cog)
        await ctx.send(f"Unloaded Extension: {cog}.py")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog):
        self.bot.reload_extension("cogs." + cog)
        await ctx.send(f"Reloaded Extension: {cog}.py")


def setup(bot):
    bot.add_cog(Control(bot))
