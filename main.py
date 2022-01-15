import nextcord
from nextcord.ext import commands
import BotConfig
import json
import os
import os.path

#intents
intents = nextcord.Intents.default()
intents.members = True

#Getting Prefix From Config File
BOTPREFIX=BotConfig.BOT_PREFIX

#Prefixes
client = commands.Bot(command_prefix = BOTPREFIX, intents=intents)
client.remove_command("help")

#Getting Bot Prefix From Config File
TOKEN=BotConfig.DISCORD_BOT_TOKEN

#Bot startup console message
@client.event
async def on_ready():
    print('Bot Logged in. {0.user}'.format(client))
    print('NOTICE: DO NOT CLOSE THIS WINDOW OR THE BOT WILL GO OFFLINE')


#Ban Command
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: nextcord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('You do not have permission to use this command!')
        return

    #Banning Member Mentioned
    await member.ban(reason=reason)

    #Confirmation Message
    await ctx.send(f'User {member.mention} has been banned. Reason: {reason}')

#Ban Errors
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't to mention a user to ban!")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("The member you mentioned was not found. Please make sure the person is still in the server!")


#Kick Command
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: nextcord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send('You do not have permission to use this command!')
        return

    #Kicking Member
    await member.kick(reason=reason)

    #Confirmation Message
    await ctx.send(f'User {member.mention} has been kicked. Reason: {reason}')

#Kick Errors
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't mention a user to kick!")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("The member you mentioned was not found. Please make sure the person is still in the server!")

client.run(TOKEN)