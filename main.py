# Import the necessary modules
import discord
import asyncio
from discord.ext import commands
from awake import awake
from replit import db
from discord import Member
import os
from discord.ui import button

# Create a new bot instance with the command prefix '-' and enable all intents
bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print("200: Bot has connected")


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

        @bot.commands()
        @button(label='Would you like to join Hunger Games?', style=discord.ButtonStyle.blurple, custom_id='Hunger games')
        async def bored(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.defer(ephemeral=True)
            
          

        @discord.ui.button(label="Send Message", style=discord.ButtonStyle.grey)
        async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("You Clicked Me!")



# @bot.command()
# async def menu(ctx):
#     view = Menu()
#     await ctx.reply("blabla", view=view)



db["channel_num"] = [1, 2, 3, 4, 5]
@bot.command()
async def create(ctx):

    if len(db["channel_num"]) > 0:
        # Grabs the next available channel
        current_num = db["channel_num"][0]
        channel_name = (f'hunger-game-{current_num}')

        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        category = discord.utils.get(guild.categories, name='DEVELOPMENT')
        user = ctx.author

        if (not existing_channel):
            overwrites = {
                ctx.guild.default_role:
                discord.PermissionOverwrite(send_messages=False),
                ctx.guild.me:
                discord.PermissionOverwrite(send_messages=True),
                ctx.author:
                discord.PermissionOverwrite(send_messages=True)
            }

            # Create channel
            await category.create_text_channel(channel_name,
                                               overwrites=overwrites)
            channel = discord.utils.get(ctx.guild.channels, name=channel_name)
            channel_id = channel.id
            channel_mention = bot.get_channel(channel_id)

            view = Menu()
            await channel_mention.send(
                f"{ctx.message.author.mention} Welcome to your Hunger Games Channel! Please await for futher instructions!", view=view
            )

            await ctx.send(
                f'The <#{channel_id}> channel has been created by {user.mention}. Have fun!',
                delete_after=15)

            # Remove current channel number from database to ensure no more than 5 channels at a time
            db["channel_num"].pop(0)
            await asyncio.sleep(3600)  # import asyncio
            await channel.delete()

        else:
            await ctx.send('That channel already exists', delete_after=15)
    else:
        await ctx.send("No Open Game Channels Left... Please Wait.",
                       delete_after=15)


#Temporary Deletion Command
@bot.command(name="deletechannel")
@commands.has_any_role('Product Owner', 'Developer')
async def deleteChannel(ctx):
    await ctx.channel.delete()


@bot.command(name="profile")
async def profile(ctx, user: Member = None):

    if user == None:
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


@bot.command(name="getid")
async def getID(ctx):
    print(ctx.author.id)


# # Defines a command called "sendtempmsg" that sends a temporary message to a specific channel
# @commands.command()
# async def sendtempmsg(ctx):
#     # Fetches the channel where the message will be sent
#     suggestions_ch = await bot.fetch_channel('1099035128107380776')
#     # Creates an embedded message with a title, description, and color
#     embed = discord.Embed(
#         title='Welcome To The Hunger Games Bot!',
#         description=
#         (f'Thank you for taking your time to test and support the up and coming best hunger games bot on the market. Please           note this has just recently began development. The team responsible for this bot are very motivated and strive for success. If            you have any suggestions please let us know by sending them in the {suggestions_ch} channel!'
#          ),
#         color=discord.Color.green())
#     # Sets the thumbnail image of the embedded message
#     embed.set_thumbnail(
#         url=
#         'https://i.pinimg.com/originals/22/4b/48/224b48c069333de9b08e615d53a3a631.jpg'
#     )
#     # Adds a field to the embedded message explaining the bot prefix and how to get started using the bot
#     embed.add_field(
#         name='Bot Prefix',
#         value=
#         'Use - to enable the use of the bot. Try using -help to get started!',
#         inline=True)
#     # Sends the embedded message to the channel where the command was executed
#     await ctx.send(embed=embed)
#     # Sends a separate message tagging everyone in the server to notify them of the new message
#     await ctx.send(content="@everyone")

#run webserver
awake()

# Start the bot with the provided bot token.
bot.run(os.environ['BOT_TOKEN'])
