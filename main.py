# Import the necessary modules
import discord
from discord.ext import commands
from awake import awake
import random
import os

# Create a new bot instance with the command prefix '-' and enable all intents
client = commands.Bot(command_prefix="-", intents=discord.Intents.all())
client.remove_command('help')


# Define an event that will be called when the bot is ready to start processing events
@client.event
async def on_ready():
    print(
        "200: Bot has connected."
    )  # Print a message to the console indicating that the bot has connected


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


@client.command()
async def begin(ctx):
    await ctx.send("Initiating Game...")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description=
        'Welcome to the help section. Here are all the Hunger Game Commands!',
        color=discord.Color.green())
    embed.set_thumbnail(
        url=
        'https://i.pinimg.com/originals/22/4b/48/224b48c069333de9b08e615d53a3a631.jpg'
    )
    embed.add_field(name='-help',
                    value='List all of the commands',
                    inline=True)

    await ctx.send(embed=embed)


@client.command()
async def sendtempmsg(ctx):
    suggestions_ch = await client.fetch_channel('1099035128107380776')
    embed = discord.Embed(
        title='Welcome To The Hunger Games Bot!',
        description=
        (f'Thank you for taking your time to test and support the up and coming best hunger games bot on the market. Please note this has just recently began development. The team responsible for this bot are very motivated and strive for success. If you have any suggestions please let us know by sending them in the {suggestions_ch} channel!'
         ),
        color=discord.Color.green())
    embed.set_thumbnail(
        url=
        'https://i.pinimg.com/originals/22/4b/48/224b48c069333de9b08e615d53a3a631.jpg'
    )
    embed.add_field(
        name='Bot Prefix',
        value=
        'Use - to enable the use of the bot. Try using -help to get started!',
        inline=True)

    await ctx.send(embed=embed),
    await ctx.send(content="@everyone")


#run webserver
awake()

# Start the bot with the provided bot token
client.run(os.environ['BOT_TOKEN'])
