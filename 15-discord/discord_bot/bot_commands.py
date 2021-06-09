import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='?')


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hey")

if __name__ == '__main__':
    bot.run(TOKEN)
