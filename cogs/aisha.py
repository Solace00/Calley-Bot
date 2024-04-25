import discord
from discord import app_commands
from discord.ext import commands


class Aisha(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Aisha Cog loaded.")

    ## Aether Sage #################################

    @commands.command(aliases = ["Aes", "aes"])
    async def AeS(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Aether Sage", colour=discord.Color.purple())

            em.set_author(name= "Aisha", url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png', icon_url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/f/f6/Icon_-_Aether_Sage.png")
            em.add_field(name="", value="**Raid Skill**, Unmod Frost Barrage (A) and unmod Lightning Shower (S) on small bosses. \n Mod A and S on big bosses. \n\n **Clearing**, can replace Blaze Step (W) with Blizzard Shower")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925352177434694/1228926213188485150/image.png?ex=662dd1b9&is=661b5cb9&hm=9a1975a2159a88b40d8ec982a3c4b74458b250b80535b3cd0e7353fa85b8ddc1&=&format=webp&quality=lossless")
            em.set_footer(text= f"Skillset from: Mafuyu")

            await ctx.send(embed = em)

    

        ## Oz master #################################

    class Menu1(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="General", style=discord.ButtonStyle.primary)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message('Button Clicked')

    @commands.command(aliases = ["Oz", "oz"])
    async def OZ(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Oz Sorcerer", colour=discord.Color.purple())

            em.set_author(name= "Aisha", url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png', icon_url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/0/0c/Icon_-_Oz_Sorcerer.png")
            em.set_image(url= "")
            em.set_footer(text= f"Skillset from: ")

            view = self.Menu1() # type: ignore
            await ctx.send(embed = em, view = view)


    ## Metamorphy #################################

    class Menu2(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="General", style=discord.ButtonStyle.primary)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.edit_message('Button Clicked')

    @commands.command(aliases = ["Mtm", "mtm"])
    async def MtM(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Metamorphy", colour=discord.Color.purple())

            em.set_author(name= "Aisha", url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png', icon_url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/4/4c/Icon_-_Metamorphy.png")
            em.set_image(url= "")
            em.set_footer(text= f"Skillset from: ")

            view = self.Menu2() # type: ignore
            await ctx.send(embed = em, view = view)   


    ## Lord Azoth #################################


    @commands.command(aliases = ["La", "la"])
    async def LA(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Lord Azoth", colour=discord.Color.purple())

            em.set_author(name= "Aisha", url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png', icon_url='https://elwiki.net/wiki/images/thumb/9/9e/Icon_-_Aisha.png/40px-Icon_-_Aisha.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/0/01/Icon_-_Lord_Azoth.png")
            em.add_field(name="", value="**Raid Support**, unmod Envelope(W). \n\n **Clearing**, Mod Envelope(W) can be replaced by Sparkling Body or Silver Tree.")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925352177434694/1228932848678076416/supp.PNG?ex=662dd7e7&is=661b62e7&hm=12c34591228feb5c269597f5ce03218eb0831a68e886c5ff966feafce6480b07&=&format=webp&quality=lossless&width=960&height=330")
            em.set_footer(text= f"Skillset from: Zirosein")

            await ctx.send(embed = em)


async def setup(bot):
    await bot.add_cog(Aisha(bot))