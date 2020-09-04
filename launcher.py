import discord
from discord.ext import commands
import os
import dotenv
import traceback
dotenv.load_dotenv()

EXTENSIONS = [
    "extensions.core",
    "extensions.event",
    "extensions.function"
]

class Launcher(commands.Bot):

    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        print(f"Starting Wikipedian...")

        for cog in EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

if __name__ == '__main__':
    bot = Launcher(command_prefix=commands.when_mentioned_or("/"))
    bot.run(os.getenv("TOKEN"))