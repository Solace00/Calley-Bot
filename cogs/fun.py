import discord
import random
from discord import app_commands
from discord.ext import commands
from time import sleep as delay

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog loaded.")

    #Avatar

    @commands.hybrid_command(aliases=["pfp", "av"])
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title=f"Avatar Link!", url=str(member.avatar.url), color=discord.Color.teal())
        embed.set_image(url=str(member.avatar.url))
        await ctx.send(embed=embed) ##, mention_author=False

    #8ball

    @commands.command(aliases=["8ball", "8b"])
    async def eightball(self, ctx, *, question):
        response = ["It is certain.", "It is decidedly so.", "without a doubt", "Yes, Definitely.",
        "you may rely on it.", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Reply haze, try again",
        "Better not tell you now", "cannot predict now.", "Don't count on it.", "My reply is a no.", "Very doubtful"]
        await ctx.send(f':8ball: Question: {question}\n :8ball: Answer: {random.choice(response)}')


    # ROLL DIE
    
    @commands.hybrid_command()
    async def roll(self, ctx, max:int):
        number = random.randint(0, max)
        await ctx.send("rolling dice . . .")
        delay(0.5)
        await ctx.send(f"rolled a **{number}**")


    # Choose command

    @commands.hybrid_command()
    async def choose(self, ctx, *, args):
        arguments = args.split(',')
        choice = random.choice(arguments)
        await ctx.send(f"🎲 | **{ctx.author.display_name}**, I choose **{choice}**")

async def setup(bot):
    await bot.add_cog(Fun(bot))