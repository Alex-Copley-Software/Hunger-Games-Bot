# Import the necessary modules
import discord
from discord.ext import commands
from awake import awake
import os

# Create a new bot instance with the command prefix '-' and enable all intents
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
bot.remove_command('help')


# Define an event that will be called when the bot is ready to start processing events
@bot.event
async def on_ready():
    print(
        "200: Bot has connected."
    )  # Print a message to the console indicating that the bot has connected


@bot.command()
async def create(ctx):
    channel_name = (f'Hunger Game host: {ctx.author}')
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    category = discord.utils.get(guild.categories, name='DEVELOPMENT')
    print(category)
    if not existing_channel:
        new_channel = await category.create_text_channel(channel_name)
        user = ctx.author  # Get the user who sent the command
        await ctx.send(
            f'The {channel_name} channel has been created in {category.name} category by {user.mention}'
        )
    else:
        await ctx.send('That channel already exists')


@bot.command(name="profile")
async def profile(ctx):
    user = ctx.message.author
    inline = True
    embed = discord.Embed(title=user.name + "#" + user.discriminator,
                          color=discord.Color.green())
    userData = {
        "Mention": user.mention,
        "Nick": user.nick,
        "Created at": user.created_at.strftime("%b %d, %Y, %T"),
        "Joined at": user.joined_at.strftime("%b %d, %Y, %T"),
        "Server": user.guild,
        "Top role": user.top_role,
    }
    for [fieldName, fieldVal] in userData.items():
        embed.add_field(name=fieldName + ":", value=fieldVal, inline=inline)
    embed.set_footer(text=f'id: {user.id}')
    userAvatar = user.display_avatar
    embed.set_thumbnail(url=userAvatar.url)
    await ctx.send(embed=embed)


# Defines a command called "begin" that sends a message indicating that the game is being initiated
@bot.command()
async def begin(ctx):
    await ctx.send("Initiating Game...")


# Defines a command called "help" that sends an embedded message listing all the available bot commands
@bot.command()
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
    embed.add_field(name='-profile',
                    value='Displays the users profile',
                    inline=True)
    # Sends the embedded message to the channel where the command was executed
    await ctx.send(embed=embed)


# Defines a command called "sendtempmsg" that sends a temporary message to a specific channel
@bot.command()
async def sendtempmsg(ctx):
    # Fetches the channel where the message will be sent
    suggestions_ch = await bot.fetch_channel('1099035128107380776')
    # Creates an embedded message with a title, description, and color
    embed = discord.Embed(
        title='Welcome To The Hunger Games Bot!',
        description=
        (f'Thank you for taking your time to test and support the up and coming best hunger games bot on the market. Please           note this has just recently began development. The team responsible for this bot are very motivated and strive for success. If            you have any suggestions please let us know by sending them in the {suggestions_ch} channel!'
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
bot.run(os.environ['BOT_TOKEN'])
