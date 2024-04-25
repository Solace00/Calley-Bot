import discord
from discord import app_commands
from discord.ext import commands


class Laby(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Laby Cog loaded.")

    ## Eternity Winter #################################

    @commands.command(aliases = ["Etw", "etw"])
    async def EtW(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Eternity Winner", colour=discord.Color.pink())

            em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/d/d0/Icon_-_Eternity_Winner.png")
            em.add_field(name="Clearing/Bossing", value="[W] Laby Bomb - can unmod if you think it wont hit much at bossing. \n [T] Mont Blanc - swap with [E] Mixsys if small boss")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229099581300539452/image.png?ex=662e732f&is=661bfe2f&hm=94bfaee9a8a723cd1a3476cde74783d0ba45cc2ecd574289020d3cdef54138ca&=&format=webp&quality=lossless&width=353&height=120")
            em.set_footer(text= f"Skillset from: Chino")

            await ctx.send(embed = em)
    

        ## Day Breaker #################################

    class Menu1(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="Raid Support", style=discord.ButtonStyle.red)
        async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Radiant Soul", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/8/85/Icon_-_Radiant_Soul.png")
                em.add_field(name="Support", value="All Skill's traits should be Gigantic/Useful/Haste/Light. \n press [V] in time with DPS' 2nd main skill cast if possible, else just press whenever its off cd. \n Always cast [A] ImHelping before any skill \n\n [C] - For procing Sot Syn. \n [Q] - is free slot, but may be helpful in some cases like Abyss. \n [S] - mod WantCandy - For procing reaper title.")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229110589968617552/image.png?ex=662e7d70&is=661c0870&hm=0a11b94405ecd253ebd1db589409218116cf241bed23ba5532e10edade22ffc3&=&format=webp&quality=lossless&width=350&height=115")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)

        @discord.ui.button(label="Freezer", style=discord.ButtonStyle.blurple)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Radiant Soul", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/8/85/Icon_-_Radiant_Soul.png")
                em.add_field(name="Freezer", value="Recommended cdr in stat - atleast 30% should be fine. \n\n [Q] - is free slot, but may be helpful in some cases like Abyss. \n [S] WantCandy  - is free slot unless u have Attack of Steel Machines title")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229111276064739550/image.png?ex=662e7e13&is=661c0913&hm=4a96da16fba4228c7968af8fa40a276e4a4a4406184a94b5672d96c576e4a515&=&format=webp&quality=lossless&width=343&height=120")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)

        @discord.ui.button(label="Clearing/Bossing", style=discord.ButtonStyle.green)
        async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Radiant Soul", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/8/85/Icon_-_Radiant_Soul.png")
                em.add_field(name="Clearing/Bossing", value="dont try to main* dps ras in raids, if you arent overgeared/properly built for that content, just dont.")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229110684466413588/image.png?ex=662e7d86&is=661c0886&hm=1eea534b6254ea9a77093c30b6ec3b39021bd424155fa72b25f888d62af9df6f&=&format=webp&quality=lossless&width=340&height=113")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)


    @commands.command(aliases = ["Ras", "ras"])
    async def RaS(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Radiant Soul", colour=discord.Color.pink())

            em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/8/85/Icon_-_Radiant_Soul.png")
            em.add_field(name="Clearing/Bossing", value="dont try to main* dps ras in raids, if you arent overgeared/properly built for that content, just dont.")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229110684466413588/image.png?ex=662e7d86&is=661c0886&hm=1eea534b6254ea9a77093c30b6ec3b39021bd424155fa72b25f888d62af9df6f&=&format=webp&quality=lossless&width=340&height=113")
            em.set_footer(text= f"Skillset from: Chino")

            view = self.Menu1() # type: ignore
            await ctx.send(embed = em, view = view)


    ## Twilight #################################


    class Menu2(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="Raid/Bossing", style=discord.ButtonStyle.red)
        async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Nisha Labyrinth", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/d/df/Icon_-_Nisha_Labyrinth.png")
                em.add_field(name="Bossing", value="[E] can be replaced with Bibi...! if pt is lacking def shred. \n [S] can be replaced for Mod Go Away! if need more cdr (for procing Wooki passive/Gain Growth Stage for cdr from Equivalent Exchange passive). \n careful using [E] Bad Dream as it will **interrupt freeze**")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229101383194509393/image.png?ex=662e74dd&is=661bffdd&hm=71034cedbdc9c284d570afb1d8d58c206ec821bc7f79152841ca64216ae6905a&=&format=webp&quality=lossless&width=338&height=112")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)

        @discord.ui.button(label="Clearing", style=discord.ButtonStyle.green)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Nisha Labyrinth", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/d/df/Icon_-_Nisha_Labyrinth.png")
                em.add_field(name="Clearing", value="[W] Wooki...! or [C] Zumyu...! - can be replaced for Poco...! for clearing elria and below regions. \n [S] Splashy - can be replaced with Suplen if need more Clearing. \n [E] Bad Dream - can be replaced with Poke It? for clearing elria and below regions")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229101247991382128/image.png?ex=662e74bd&is=661bffbd&hm=c44e2438ec1a0f7a2d9ee7f15fd0b3019df45358e9e653d2556f9e48a539ad73&=&format=webp&quality=lossless&width=351&height=111")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)


    @commands.command(aliases = ["Nl", "nl"])
    async def NL(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Nisha Labyrinth", colour=discord.Color.pink())

            em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/d/df/Icon_-_Nisha_Labyrinth.png")
            em.add_field(name="Clearing", value="[W] Wooki...! or [C] Zumyu...! - can be replaced for Poco...! for clearing elria and below regions. \n [S] Splashy - can be replaced with Suplen if need more Clearing. \n [E] Bad Dream - can be replaced with Poke It? for clearing elria and below regions")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229101247991382128/image.png?ex=662e74bd&is=661bffbd&hm=c44e2438ec1a0f7a2d9ee7f15fd0b3019df45358e9e653d2556f9e48a539ad73&=&format=webp&quality=lossless&width=351&height=111")
            em.set_footer(text= f"Skillset from: Chino")

            view = self.Menu2() # type: ignore
            await ctx.send(embed = em, view = view)


    ## Prophetess #################################


    class Menu3(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.Value = None

        @discord.ui.button(label="Raid/Bossing", style=discord.ButtonStyle.red)
        async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Twins Picaro", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/d/d4/Icon_-_Twins_Picaro.png")
                em.add_field(name="Bossing", value="Spam V key to maximize gaining Black Aura. \n Try to get hit while casting HA2 [Lshift], it will cancel the animation.")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229099956300943481/image.png?ex=662e7389&is=661bfe89&hm=971a39f37a6349701ab07ed5cd023960ed7b83ba518ce7d974a67fffef48247d&=&format=webp&quality=lossless&width=348&height=111")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)

        @discord.ui.button(label="Clearing", style=discord.ButtonStyle.green)
        async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
                em = discord.Embed(title = "Twins Picaro", colour=discord.Color.pink())

                em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
                em.set_thumbnail(url="https://elwiki.net/wiki/images/d/d4/Icon_-_Twins_Picaro.png")
                em.add_field(name="Clearing", value="[S] I'm Fine - can be modded. \n [W] Long Stocking - can be replaced with Laby School or Whole Train if not needed. \n [T] Coloring Fun - can be moded if prefer or have enough dmg")
                em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229099902022324364/image.png?ex=662e737c&is=661bfe7c&hm=b73f9b2a665250d48f0d8ab50f21ab0dafa6bb1d6586b4265b8c81eb06d3234d&=&format=webp&quality=lossless&width=363&height=123")
                em.set_footer(text= f"Skillset from: Chino")

                await interaction.response.edit_message(embed=em)


    @commands.command(aliases = ["Twp", "twp"])
    async def TwP(self, ctx, member:discord.Member = None):
            em = discord.Embed(title = "Twins Picaro", colour=discord.Color.pink())

            em.set_author(name= "Laby", url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png', icon_url='https://elwiki.net/wiki/images/1/16/Icon_-_Laby.png')
            em.set_thumbnail(url="https://elwiki.net/wiki/images/d/d4/Icon_-_Twins_Picaro.png")
            em.add_field(name="Clearing", value="[S] I'm Fine - can be modded. \n [W] Long Stocking - can be replaced with Laby School or Whole Train if not needed. \n [T] Coloring Fun - can be moded if prefer or have enough dmg")
            em.set_image(url= "https://media.discordapp.net/attachments/1228925756776644759/1229099902022324364/image.png?ex=662e737c&is=661bfe7c&hm=b73f9b2a665250d48f0d8ab50f21ab0dafa6bb1d6586b4265b8c81eb06d3234d&=&format=webp&quality=lossless&width=363&height=123")
            em.set_footer(text= f"Skillset from: Chino")

            view = self.Menu3() # type: ignore
            await ctx.send(embed = em, view = view)


async def setup(bot):
    await bot.add_cog(Laby(bot))