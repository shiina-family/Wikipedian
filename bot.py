import glob
import os
import traceback

import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv()


class Wikipedian(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("/"))
        print("Starting Wikipedian...")

        for cog in [cog.replace("/", ".").replace(".py", "")
                    for cog in glob.glob("cogs/*.py")]:
            try:
                self.load_extension(cog)
                print(f"loaded: {cog}")
            except BaseException:
                traceback.print_exc()

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.BadArgument):
            return
        await ctx.send(error)

    async def on_ready(self):
        user = self.user
        print("logged in:", str(user), user.id)
        game = discord.Game(name=str(user) + " | Use /wiki <title>")
        await self.change_presence(activity=game)


if __name__ == '__main__':
    bot = Wikipedian()
    bot.run(os.getenv("TOKEN"))
