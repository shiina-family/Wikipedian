from discord.ext import commands


class Control(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not await ctx.bot.is_owner(ctx.author):
            await ctx.send("You don't have permission.")
            return False
        return True
    
    @commands.command()
    async def load(self, ctx, cog):
        self.bot.load_extension("cogs." + cog)
        await ctx.send(f"Loaded Extension: {cog}.py")

    @commands.command()
    async def unload(self, ctx, cog):
        if cog == "control":
            await ctx.send("You can't unload it!")
        self.bot.unload_extension("cogs." + cog)
        await ctx.send(f"Unloaded Extension: {cog}.py")

    @commands.command()
    async def reload(self, ctx, cog):
        self.bot.reload_extension("cogs." + cog)
        await ctx.send(f"Reloaded Extension: {cog}.py")


def setup(bot):
    bot.add_cog(Control(bot))
