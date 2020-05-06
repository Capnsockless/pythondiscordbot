from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!", status=discord.Status.do_not_disturb, activity=discord.Game(name="Booting.."))

@bot.event
async def on_ready():
    print("Ready to go!")
    print(f"Serving: {len(bot.guilds)} guilds.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="!help for commands"))

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is {ping}ms")

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")

@bot.command()
async def pingall(ctx):
    await ctx.channel.send("@everyone")

@bot.command()
async def meme(ctx):
    await ctx.channel.send("<@671061763634102342>'s life.")

@bot.command()
async def urmomgay(ctx):
    await ctx.channel.send("Poggers")

@bot.command()
async def kick(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick yourself!")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been kicked from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member} has been kicked!")    

@bot.command()
async def matthewsimpingouthere(ctx):
    await ctx.channel.send("<@!602546423124459560> be simping over <@!400333714036621344> out here lmfao.")

@bot.command()
async def whoisasimp(ctx):
    await ctx.channel.send("The simps are: <@!602546423124459560> and <@!671061763634102342>.")

bot.run("NzA2ODIxNzA5OTQ4NTE4NDAx.Xq_1bQ.MODQ2Ur_IS1Gayr4l1GVTGxFTKc")