import asyncio
from discord.ext import commands
#from discord.ext.commands import *
import discord as d
import os
import requests
import random 
import os
import os.path


from lists import rate_me_scale
from lists import laugh_words
from lists import bad_words
from lists import bot_laughs
from lists import sorry_words
from lists import thank_words
from lists import yummy_foods
from lists import bot_responses
from lists import kind_words
from lists import swear_corrections
from lists import emoji_foods
from lists import emoji_reactions
from lists import opinion_agreement

invitere2 = r"(http[s]?:\/\/)*discord((app\.com\/invite)|(\.gg))\/(invite\/)?(#\/)?([A-Za-z0-9\-]+)(\/)?"

async def change(self, ctx):
  if ctx.invoked_subcommand is None:
    await ctx.send_help(str(ctx.command))

    
commandlist = ["joke", "help", "test", "delete channel"]

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&format=txt&type=twopart")
  joke = response.text 
  return(joke)

client  = d.Client()
client = commands.Bot(command_prefix=".g ")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        'Hello there {member.name}, welcome! My name is Globot and I am a helper here. I tell jokes and answer crystal ball questions.'
    )


@client.event
async def on_ready():
  print('Login: {0.user}'.format(client))


@client.command()
async def test(ctx): 
  await ctx.send('Globot has arrived!')


@client.command()
async def joke(ctx): 
  joke = get_joke()
  await ctx.send(joke)
  
@client.command()
async def commands(ctx): 
  for x in commandlist:
   await ctx.send(x)

@client.command()
async def nukeping88(ctx, times: int, content="@best bot"):
    for i in range(times):
        await ctx.send(content)

@client.command()
async def ris(ctx, times: int, content="ris"):
    for i in range(times):
        await ctx.send(content)

@client.command()
async def deletechannel(ctx, channel: d.TextChannel):
  mbed = d.Embed(
    title = 'Success',
    description = f'Channel: {channel} has been deleted',
  )
  if ctx.author.guild_permissions.manage_channels:
    await ctx.send(embed=mbed)
    await channel.delete()


@client.command()
async def createchannel(ctx, channelName):
  guild = ctx.guild

  mbed = d.Embed(
    title = 'Success',
    description = "{} has been successfully created.".format(channelName)
  )
  if ctx.author.guild_permissions.manage_channels:
    await guild.create_text_channel(name = '{}'.format(channelName))
    await ctx.send(embed=mbed)

@client.command()
async def say(ctx, *args):
  response = ""
  for arg in args:
	  response = response + " " + arg
  await ctx.channel.send(response)

@client.command()
async def roll(ctx, dice: str):
    """nout my code"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@client.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

#snipe command
client.sniped_messages = {}
@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("No recently deleted messages")
        return

    embed = d.Embed(description=contents, color=d.Color.purple(), timestamp=time)
    embed.set_author(name=f"Sent by: {author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)
#other commands
@client.command()
async def _8ball(ctx, *, question):
  crystal_ball = ["yes", "no", "maybe", "hmm, ask again", "i cannot answer that", "definitley not","absolutley yes!", "✅"]
  await ctx.send('*Welcome to the Globot Crystal Ball Service:*')
  await ctx.send(f'You asked: {question}\nAnswer: {random.choice(crystal_ball)}')


client.run(os.getenv('TOKEN'))