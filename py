import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! I am {bot.user}!')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)


@bot.command()
async def help_(ctx):
    await ctx.send('Functions i have:\n'
                   '$hello - bot is greeting you\n'
                   '$add - adds up yo numbers\n'
                   '$heh - write how many times the bot needs to repeat "heh"\n'
    )
                   
bot.run("your token")
