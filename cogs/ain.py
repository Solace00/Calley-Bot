import discord
from discord import app_commands
from discord.ext import commands


class Ain(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ain Cog loaded.")

    ## Anemos #################################

    class Menu(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="Raid/Bossing", style=discord.ButtonStyle.red)
        async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Richter", colour=discord.Color.blue())

                em.set_author(name= "Ain", url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png', icon_url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/e/e3/Icon_-_Richter.png")
                em.add_field(name="Raid", value="Mod Brocken Aushauen(D).")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925731837317160/1228961526002487326/image.png?ex=662df29c&is=661b7d9c&hm=7eb1fef87b362713a2034a244c3012714bf88ea2622705d64231f47975b56c99&=&format=webp&quality=lossless")
                em.set_footer(text= f"Skillset from: Met")

                await interaction.response.edit_message(embed=em)

        @discord.ui.button(label="Clearing", style=discord.ButtonStyle.green)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Richter", colour=discord.Color.blue())

                em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png', icon_url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/e/e3/Icon_-_Richter.png")
                em.add_field(name="Clearing", value="")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925731837317160/1228961476576940113/image.png?ex=662df291&is=661b7d91&hm=c03f21340308050c3f7f32aa773f65fc06aa7f6adf2a1ff5bfd92a889ef4252f&=&format=webp&quality=lossless")
                em.set_footer(text= f"Skillset from: Met")

                await interaction.response.edit_message(embed=em)


    @commands.command(aliases = ["Rt", "rt"])
    async def RT(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Richter", colour=discord.Color.blue())

            em.set_author(name= "Ain", url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png', icon_url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/e/e3/Icon_-_Richter.png")
            em.add_field(name="Raid", value="Mod Brocken Aushauen(D).")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925731837317160/1228961526002487326/image.png?ex=662df29c&is=661b7d9c&hm=7eb1fef87b362713a2034a244c3012714bf88ea2622705d64231f47975b56c99&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Met")

            view = self.Menu() # type: ignore
            await ctx.send(embed = em, view = view)
    

        ## Day Breaker #################################


    @commands.command(aliases = ["Bl", "bl"])
    async def BL(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Bluhen", colour=discord.Color.blue())

            em.set_author(name= "Ain", url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png', icon_url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/7/7c/Icon_-_Bluhen.png")
            em.add_field(name="", value="")
            em.set_image(url= "")
            em.set_footer(text= f"Skillset from: ")

            await ctx.send(embed = em)


    ## Twilight #################################


    @commands.command(aliases = ["Hr", "hr"])
    async def HR(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Herrscher", colour=discord.Color.blue())

            em.set_author(name= "Ain", url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png', icon_url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/1/18/Icon_-_Herrscher.png")
            em.add_field(name="Bossing/Clearing", value="Mod Befreiung Feld(R)")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925731837317160/1228961672740208660/image.png?ex=662df2bf&is=661b7dbf&hm=cd8997c65c0db9994f7b15f85a9b8e0b5b50affbe81b7ba869bfa5464fa7abce&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Met")

            await ctx.send(embed = em) 


    ## Prophetess #################################


    @commands.command(aliases = ["Bg", "bg", "OP", "op", "Op", "OfG", "Ofg"])
    async def BG(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Opferung/Bigott", colour=discord.Color.blue())

            em.set_author(name= "Ain", url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png', icon_url='https://elwiki.net/wiki/images/1/17/Icon_-_Ain.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/8/84/Icon_-_Opferung.png")
            em.add_field(name="Bossing/Clearing", value="**For Clearing**, unmod Wegnahme(D)")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925731837317160/1228961772766232607/image.png?ex=662df2d7&is=661b7dd7&hm=48084da480acb18f4c5c2e2715fb0b672844dc4164b0cbb26427bf3d331f5f92&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Met")

            await ctx.send(embed = em)


async def setup(bot):
    await bot.add_cog(Ain(bot))