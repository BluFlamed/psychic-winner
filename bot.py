import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event 
async def on_ready():
    print ("Hello World")
    print ("im running on " + bot.user.name)
    print ("with the ID:" + bot.user.id)

@bot.command(pass_context=True)
async def blu(ctx):
    await bot.say("<:feelsgoodman:508717183812239401> peepeepoopoo")


@bot.command(pass_context=True)
async def altihag(ctx):
    await bot.say("more like alticat")

@bot.command(pass_context=True)
async def bluflamed(ctx):
    await bot.say("more like pooflamed")

@bot.command(pass_context=True)
async def ding(ctx):
    await bot.say("dong!!!")

bot.run ("NTA4NDkxMjg2NjM5MDE3OTg0.DsDSGA.24YgP7vo8KDOT22YhEcyEWQTdtA")










