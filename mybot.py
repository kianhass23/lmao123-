# Import discord package
import discord
import random
from discord.ext import commands
import asyncio

# Client bot
client = commands.Bot(command_prefix='.')
client.snipe_messages = {}
client.remove_command('help')



@client.command(name='yo')
async def version(context):




   # DO STUFF

   general_channel = client.get_channel(817706086484279326)
   await general_channel.send('e')





@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member.mention}**KICKED!:thumbsup:**")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member.mention}**BANNED! :thumbsup:**")

@client.command()
async def help(ctx):
   helpembed=discord.Embed(title='**[🤖] BOT COMMANDS**', description='**[MODERATION]**', colour=random.randint(0, 0xffffff))
   helpembed.add_field(name='[⚠️] BAN MEMBER', value='**cmd = !ban**')
   helpembed.add_field(name='[👾] KICK MEMBER', value='**cmd = !kick**')
   helpembed.add_field(name='[🤐] MUTE MEMBER', value='**cmd = !mute**')
   helpembed.add_field(name='[☠️] ADDING MORE..', value='**cmd = NONE**')
   


   await ctx.send(embed=helpembed)



@client.command()
async def ping(ctx):
   await ctx.send('f**PONG!**')


 


# Run the client on the server
client.run('ODE5MTA5OTUxNTgxNDU0MzU2.YEh1lg.i-DxAuLKtpIoLZXlbhmtioS-TY0')