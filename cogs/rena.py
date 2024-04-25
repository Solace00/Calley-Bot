import discord
from discord import app_commands
from discord.ext import commands


class Rena(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Rena Cog loaded.")

    ## Anemos #################################

    @commands.command(aliases = ["An", "an"])
    async def AN(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Anemos", colour=discord.Color.green())

            em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png', icon_url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/2/21/Icon_-_Anemos.png")
            em.add_field(name="", value="**Raid Skill set**, Mod Dive Kick(F) Bombing on big bosses. \n\n **Clearing**, replace either Aero Tornado (E) or Sharp Fall (A) with Phoenix Strike")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925353842442290/1228927738547540078/image.png?ex=662dd325&is=661b5e25&hm=52242a4fed879c4550ccb7cc1e31cb48913792fc137b01ab38767eb11d963d61&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Ivy")

            await ctx.send(embed = em)
    

        ## Day Breaker #################################


    @commands.command(aliases = ["dab", "Dab"])
    async def DaB(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "DayBreaker", colour=discord.Color.green())

            em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png', icon_url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/3/36/Icon_-_Daybreaker.png")
            em.add_field(name="", value="**Raid**, Except for Ace in the Hole (F) and the 3 actives skills (S, D, C), can bring any other special active skills.\n\n **Clearing**, Replace Aero Tornado with Phoenix Strike.")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925353842442290/1228927844638527521/image.png?ex=662dd33e&is=661b5e3e&hm=242d2e20ee3c01c0e099cf5ef54e195d2976a5a38036110edcf4198c4abfb04c&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Ivy")

            await ctx.send(embed = em)


    ## Twilight #################################


    @commands.command(aliases = ["Tw", "tw"])
    async def TW(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Twilight", colour=discord.Color.green())

            em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png', icon_url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/0/09/Icon_-_Twilight.png")
            em.add_field(name="", value="**Raid**, Mod Karma(Lshift) on small bosses, unmod Karma(LShift) on big bosses. \n\n **Clearing**,  replace either Fatality (Q) or Gliding Strike (A) with Phoenix Strike.")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925353842442290/1228927955611156550/image.png?ex=662dd358&is=661b5e58&hm=0bbe5bb6be9fec8cf85e3fd19eb89e98477b4aef954ae54a664a1f12be7353d2&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Ivy")

            await ctx.send(embed = em) 


    ## Prophetess #################################

    class Menu3(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="Raid/Bossing", style=discord.ButtonStyle.red)
        async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Prophetess", colour=discord.Color.green())

                em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png', icon_url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/6/6d/Icon_-_Prophetess.png")
                em.add_field(name="Raid", value="Unmod Expansion (W) on big bosses. Unmod Recite (Lshift) on small bosses. \n Can replace W with Perfect Storm if you dont plan on dps with her. \n\n **For V key**, \n Roll for MP recovery upon using special active skills (if there is only one healer in the party besides you).\n Apply an action speed buff upon using active skills if your party needs it.\n Alternatively, provide an attack buff upon using MC skills if you want more DPS support rather than utility.")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925353842442290/1228928111794585681/image.png?ex=662dd37e&is=661b5e7e&hm=47574d6ca3128a05c55a6ee9d06bc757e6deb6a9cb8c9900d74a3f931f9607ac&=&format=webp&quality=lossless")
                em.set_footer(text= f"Skillset from: Ivy")

                await interaction.response.edit_message(embed=em)

        @discord.ui.button(label="Clearing", style=discord.ButtonStyle.green)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Prophetess", colour=discord.Color.green())

                em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png', icon_url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/6/6d/Icon_-_Prophetess.png")
                em.add_field(name="Clearing", value="Generally can replace W and A with any strength skills, however those 2 are the most efficient. \n\n **For V key**, roll for MP recovery upon using special active skills.")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925353842442290/1228928086838612050/image.png?ex=662dd378&is=661b5e78&hm=049a2267640906d440e64a22f55a1e55a8f540a9e33e6d1aba9730c18d48a522&=&format=webp&quality=lossless")
                em.set_footer(text= f"Skillset from: Ivy")

                await interaction.response.edit_message(embed=em)


    @commands.command(aliases = ["Pr", "pr"])
    async def PR(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Prophetess", colour=discord.Color.green())

            em.set_author(name= "Rena", url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png', icon_url='https://elwiki.net/wiki/images/6/67/Icon_-_Rena.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/6/6d/Icon_-_Prophetess.png")
            em.add_field(name="Raid", value="Unmod Expansion (W) on big bosses. Unmod Recite (Lshift) on small bosses. \n Can replace W with Perfect Storm if you dont plan on dps with her. \n\n **For V key**, \n Roll for MP recovery upon using special active skills (if there is only one healer in the party besides you).\n Apply an action speed buff upon using active skills if your party needs it.\n Alternatively, provide an attack buff upon using MC skills if you want more DPS support rather than utility.")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925353842442290/1228928111794585681/image.png?ex=662dd37e&is=661b5e7e&hm=47574d6ca3128a05c55a6ee9d06bc757e6deb6a9cb8c9900d74a3f931f9607ac&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Ivy")

            view = self.Menu3() # type: ignore
            await ctx.send(embed = em, view = view)


async def setup(bot):
    await bot.add_cog(Rena(bot))