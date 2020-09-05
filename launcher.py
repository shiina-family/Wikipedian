import glob
import discord
from discord.ext import commands
import os
import dotenv
import traceback
dotenv.load_dotenv()


class Launcher(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("/"))
        print(f"Starting Wikipedian...")

        for cog in [cog.replace("/", ".").replace(".py", "") for cog in glob.glob("extensions/*.py")]:
            try:
                self.load_extension(cog)
                print(f"loaded: {cog}")
            except:
                traceback.print_exc()


if __name__ == '__main__':
    bot = Launcher()
    bot.run(os.getenv("TOKEN"))
