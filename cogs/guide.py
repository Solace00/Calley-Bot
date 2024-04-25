import discord
import random
from discord import app_commands
from discord.ext import commands
from time import sleep as delay

class Guide(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Guide Cog loaded.")

    @commands.hybrid_command(description="This command provides you with all the available general guides about elsword.")
    async def general(self, ctx):
        em = discord.Embed(title = "General Guides", description = "Here are some helpful guides", color=discord.Color.pink())

        em.add_field(
            name = "",
            value = "**🔗[Complete In-Depth Progression Guide to Elsword](https://docs.google.com/document/d/1F-ClyjAEWh0VFaye9boSPfm_ZXgGjiJmTi5P87sA4A8/edit#heading=h.4hnkw3xxg5b3)** \n Walkthrough guide of how to reach end game efficiently. \n**Author** Rinya [Aquila Guild - NA] ",
            inline = False
        )
        
        em.add_field(
            name = "",
            value = "**🔗[Reforge Costs for Tenebrous Armor](https://docs.google.com/spreadsheets/d/14N1QygpFBlP1b7gsyDaVzAIvaQUm7kxINfKks_-BbKg/edit#gid=1890228228)** \n Material costs for reforging post. Updated after QoL. \n**Author** KoG",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Raid Buffs for Potatos](https://docs.google.com/document/d/1rGlzynf72X58kbKAoGq8Ym2cR_W2Foqe7jOTGNYflzU/edit)** \n A list of buffs and debuffs for each character. \n**Author** Kalmias",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Very Brief Guide to Traits](https://docs.google.com/document/d/1SHu9zatu7kTyb-dVCxJ4gNUlpHkJDuJYpZnFGfJMS80/edit#heading=h.v69ku9dimyhg)** \n Brief explanation of each skill trait and recommendations on which to pick. \n**Author** Unknown",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[What the f* to do in elsword 1~3m cp edition](https://docs.google.com/document/d/1I24mls1nFKfUlhXowHTksFDekN-Ik7lqvWQdG1SJr3A/edit#heading=h.4inltu7hdkw)** \n Brief explanation of what to do in elsword if you feel stuck. \n**Author** Anonymous",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Consumable/Elixir Guide](https://docs.google.com/document/d/1sMmsSQ5enVLsz2FY9qREVCiO8IAP_DcyqXXgQ5Rw9E4/edit)** \n Brief information about consumables and elixirs. \n**Author** Unknown",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Guide to Increasing your EXP gain](https://docs.google.com/document/d/1RAfihMzMGt_7nCPPtLiKbv-oAI0KNMvPwN3_PlB2wCs/edit)** \n Brief explanation about increasing your exp gain. \n**Authors** zack, Retoure, imHalcyon, KimiChuu and Arvisna",
            inline = False
        )

        await ctx.send(embed = em)


## GEAR guide   #################################################################

    @commands.hybrid_command(description="This command provides you with all the available gear guides about elsword.")
    async def gear(self, ctx):
        em = discord.Embed(title = "Gear Guides", description = "Here are some helpful gear guides", color=discord.Color.pink())

        em.add_field(
            name = "",
            value = "**🔗[Tenebrous Armor Guide](https://docs.google.com/document/d/1h_f_mpzKjIjPVC_YZeVI_PLwosgsFzfRn5_LG0yYBUI/edit#heading=h.8c69hlhw17yr)** \n Brief explaination on Tenebarous Armor set and shadow effects. \n**Author** Originally Zack and continued by mommyhanaka",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Critcal and Maximize Guide](https://docs.google.com/spreadsheets/d/e/2PACX-1vQkHyGXROrJ0TUrax6T5h2Sc0dta9p3xCh-Jwl_z_4l22bEEB44k03xZ9tSfvnpZWyTHTgYYqN-tFIV/pubhtml#)** \n Optimal values for these stats for each character. \n**Author** Unknown",
            inline = False
        )


        em.add_field(
            name = "",
            value = "**🔗[Artifact Spirit Stone Guide](https://docs.google.com/document/d/1isPeL7J_35dSCzVinGPpYp0KyhFKI32ruY7-a6jUDmw/edit)** \n Brief explaination on how Artifact effects work and what you need. \n**Author** Unknown",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Ashal Calculator](https://www.ashal.eu/calcs/equip)** \n A Calculator to calculate your character stats. \n**Author** Ashallia",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Reforge Calculator](https://www.elrioslab.com/en/tools/reforge)** \n A calculator to calculate approx cost it'll take to finish your reforge. \n**Author** Elrioslab",
            inline = False
        )

        await ctx.send(embed = em)


## Raid/Boss Guide #################################

    @commands.hybrid_command(description="This command provides you with all the available raid/boss guides about elsword.")
    async def raid(self, ctx):
        em = discord.Embed(title = "Raid/Boss Guides", description = "Here are some helpful Raid/Boss guides", color=discord.Color.pink())

        em.add_field(
            name = "",
            value = "**🔗[The Great Steel Wall](https://docs.google.com/document/d/12FHO1YhMSCL4GNzhyN8JYSlDoDiGJ9sgC58lcjpmH44/edit)** \n Brief explaination on how wall works. \n**Author** Unknown",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Guide for Ran Raid](https://docs.google.com/document/d/1F9MmbN-OmHwEsROH9f_6hwbr3emcTu8KZqpKQdPOKXY/edit)** \n Brief explaination on how Abyss raid works and mechs. \n**Author** berris",
            inline = False
        )

        em.add_field(
            name = "",
            value = "**🔗[Rosso (Challenge) Guide](https://docs.google.com/document/d/1i-RxMTi-_f3l3GyLtvozvc36Xg0Hh3ESNerDzfqdJd0/edit)** \n Brief explaination on how Rosso CM works and mechs. \n**Authors** Jedzter, Ketsuo, CDawg, and Cear",
            inline = False
        )

        await ctx.send(embed = em)


async def setup(bot):
    await bot.add_cog(Guide(bot))