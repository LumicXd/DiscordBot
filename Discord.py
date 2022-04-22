import string
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot Is Ready")


@client.command()
async def commands(ctx):
    await ctx.send(f"!Ping, !rice, !8ball")


@client.command(aliases=["2Yard", "2yard"])
async def _2Yard(ctx):
    await ctx.send(f"Twitch Stream https://www.twitch.tv/2yard")

@client.command()
async def secretcommand(ctx):
    await ctx.send(f"You Found The Secret Command! Like Bruh")


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="👌general")
    await channel.send(f"Welcome {member.mention}")
    print(f"{member.name} has joined a server")


@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="👌general")
    await channel.send(f"{member.mention} Has Left The Server F's In Chat")
    print(f"{member} has left a server")


@client.command
async def rice(ctx):
    await ctx.send("Eat Rice!")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {round(client.latency * 1000)}ms")


@client.command(aliases=["8ball", "8Ball"])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don’t count on it.",
                 "It is certain.",
                 "It is decidedly so.",
                 "Most likely.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Outlook good.",
                 "Reply hazy, try again.",
                 "Signs point to yes.",
                 "Very doubtful.",
                 "Without a doubt.",
                 "Yes.",
                 "Yes – definitely.",
                 "You may rely on it."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


client.run("Bot Token here")
