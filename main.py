# Import the necessary modules
import discord
import asyncio
from discord.ext import commands
from awake import awake
import os

# Create a new bot instance with the command prefix '-' and enable all intents
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
bot.remove_command('help')


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    await bot.start(os.environ['BOT_TOKEN'])


#run webserver
awake()

# Start the bot with the provided bot token.
asyncio.run(main())
