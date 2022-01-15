import nextcord
from nextcord.ext import commands
import BotConfig
import json
import os
import os.path

#Fetching Logging Channel
def get_log(client, message):
    with open(r'logs.json', 'r') as f:
        logs = json.load(f)

    return logs[str(message.guild.id)]

#intents
intents = nextcord.Intents.default()
intents.members = True

#Getting Prefix From Config File
BOTPREFIX=BotConfig.BOT_PREFIX

#Prefixes
client = commands.Bot(command_prefix = BOTPREFIX, intents=intents)
client.remove_command("help")

#Finding File Directory
directory = os.path.dirname(__file__)

#Getting Bot Prefix From Config File
TOKEN=BotConfig.DISCORD_BOT_TOKEN

#Bot startup console message
@client.event
async def on_ready():
    print('Bot Logged in. {0.user}'.format(client))
    print('NOTICE: DO NOT CLOSE THIS WINDOW OR THE BOT WILL GO OFFLINE')

#Logging Channel Actions
#Creating logging channel file when the bot joins a server
@client.event
async def on_guild_join(guild):
    f = open(f"{directory}\\Logs\\{guild.id}", 'w+')
    f.write("None")
    f.close

#Removing file when bot leaves the server
@client.event
async def on_guild_remove(guild):
    os.remove(f"{directory}\\Logs\\{guild.id}")
    print(f"{guild.id} was removed from logs")

#Setting the logging channel command
@client.command(aliases=['setlogchannel'])
async def logchannel(ctx, *, logset=None):
    if (not ctx.author.guild_permissions.administrator):
        await ctx.send('You do not have permission to use this command!')
        return

    if (logset == None):
        logset = 'None'
        await ctx.send("You did not mention or send a channel id. Logging channel has been disabled")
        return

    check = logset[:2]
    if check == "<#":
        l = len(logset)
        check2 = logset[:l-1]
        check2 = check2[2:]
        logset = check2
        print(logset)

    file_exists = os.path.exists(f'{directory}\\Logs\\{ctx.guild.id}.txt')
    if (file_exists == True):
        os.remove(f"{directory}\\Logs\\{ctx.guild.id}")
        f = open(f"{directory}\\Logs\\{ctx.guild.id}", "w+")
        f.write(f"{logset}")
        f.close
    if (file_exists == False):
        f = open(f"{directory}\\Logs\\{ctx.guild.id}", "w+")
        f.write(f"{logset}")
        f.close
    await ctx.send(f"Logging Channel set to <#{logset}>.")

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

    #Sending Logging Message
    f = open(f"{directory}\\Logs\\{ctx.guild.id}", 'r')
    if f.mode == 'r':
        logs = await ctx.guild.audit_logs(limit=1, action=nextcord.AuditLogAction.ban).flatten()
        contents = f.read()
        contentsint = int(contents)
        channel = client.get_channel(contentsint)
        logs = logs[0]
        await channel.send(f"{member.mention} was banned by {ctx.author.mention}. Reason: {reason}")
        f.close
    elif f.mode != 'r':
        f.close
        return

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

    #Sending Logging Message
    f = open(f"{directory}\\Logs\\{ctx.guild.id}", 'r')
    if f.mode == 'r':
        logs = await ctx.guild.audit_logs(limit=1, action=nextcord.AuditLogAction.ban).flatten()
        contents = f.read()
        contentsint = int(contents)
        channel = client.get_channel(contentsint)
        logs = logs[0]
        await channel.send(f"{member.mention} was kicked by {ctx.author.mention}. Reason: {reason}")
        f.close
    elif f.mode != 'r':
        f.close
        return

#Kick Errors
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't mention a user to kick!")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("The member you mentioned was not found. Please make sure the person is still in the server!")

client.run(TOKEN)