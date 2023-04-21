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


# Defines a command called "ping" that responds with "Pong!"
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


# Defines a command called "begin" that sends a message indicating that the game is being initiated
@client.command()
async def begin(ctx):
    await ctx.send("Initiating Game...")


# Defines a command called "help" that sends an embedded message listing all the available bot commands
@client.command()
async def help(ctx):
    # Creates an embedded message with a title, description, and color
    embed = discord.Embed(
        title='Bot Commands',
        description=
        'Welcome to the help section. Here are all the Hunger Game Commands!',
        color=discord.Color.green())
    # Sets the thumbnail image of the embedded message
    embed.set_thumbnail(
        url=
        'https://i.pinimg.com/originals/22/4b/48/224b48c069333de9b08e615d53a3a631.jpg'
    )
    # Adds a field to the embedded message listing the "-help" command and its purpose
    embed.add_field(name='-help',
                    value='List all of the commands',
                    inline=True)
    # Sends the embedded message to the channel where the command was executed
    await ctx.send(embed=embed)


# Defines a command called "sendtempmsg" that sends a temporary message to a specific channel
@client.command()
async def sendtempmsg(ctx):
    # Fetches the channel where the message will be sent
    suggestions_ch = await client.fetch_channel('1099035128107380776')
    # Creates an embedded message with a title, description, and color
    embed = discord.Embed(
        title='Welcome To The Hunger Games Bot!',
        description=
        (f'Thank you for taking your time to test and support the up and coming best hunger games bot on the market. Please note this has just recently began development. The team responsible for this bot are very motivated and strive for success. If you have any suggestions please let us know by sending them in the {suggestions_ch} channel!'
         ),
        color=discord.Color.green())
    # Sets the thumbnail image of the embedded message
    embed.set_thumbnail(
        url=
        'https://i.pinimg.com/originals/22/4b/48/224b48c069333de9b08e615d53a3a631.jpg'
    )
    # Adds a field to the embedded message explaining the bot prefix and how to get started using the bot
    embed.add_field(
        name='Bot Prefix',
        value=
        'Use - to enable the use of the bot. Try using -help to get started!',
        inline=True)
    # Sends the embedded message to the channel where the command was executed
    await ctx.send(embed=embed)
    # Sends a separate message tagging everyone in the server to notify them of the new message
    await ctx.send(content="@everyone")


#run webserver
awake()

# Start the bot with the provided bot token.
client.run(os.environ['BOT_TOKEN'])
