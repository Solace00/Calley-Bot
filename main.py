import discord
import os
import asyncio
import json
from discord import app_commands
from discord.ext import commands, tasks
from itertools import cycle

with open('config.json', 'r') as f:
    data = json.load(f)
token = data['tokens']['bot_token']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents = intents, help_command=None)


bot_status = cycle(["Prefix for Bot !", "Type in !help", "Developed by: le_frenny"])

@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("am online cutie.")
    change_status.start()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error: Missing Required Arguments. Are you sure you provided __all__ required arguments")

async def load():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

################### HELP ##########################################

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "help commands duh", color = 0x000000)

    em.add_field(name = "Roleplay", value = "")
    em.add_field(name = "Information", value = "Avatar")
    em.add_field(name = "Fun", value = "choose, 8ball, roll")

    await ctx.send(embed = em)

#####################################################################


async def main():
    await load ()
    await bot.start(token)

asyncio.run(main())