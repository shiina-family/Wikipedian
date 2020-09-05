from discord.ext import commands
import discord
import dotenv
import glob
import os
import traceback

dotenv.load_dotenv()

class Wikipedian(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("/"))
        print(f"Starting Wikipedian...")

        for cog in [os.path.basename for cog in glob.glob("extensions/*.py")]:
            try:
                self.load_extension(cog)
                print(f"loaded: {cog}")
            except:
                traceback.print_exc()

    async def on_command_error(self, ctx, error):
        await ctx.send(error)

    async def on_ready(self):
        user = self.user
        print("logged in:", str(user), user.id)
        game = discord.Game(name=str(user)+" | Use /wiki <title>")
        await self.change_presence(activity=game)

if __name__ == '__main__':
    bot = Wikipedian()
    bot.run(os.getenv("TOKEN"))
