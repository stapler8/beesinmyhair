# Import Dependencies
import random

import discord
from discord.ext import commands


class Messaging(commands.Cog):

    # Upon instantiation, set local variable bot to bot entity
    def __init__(self, bot):
        self.bot = bot

    # Gives a user a Gayness rating of 0-100. Note that Baraboomba is defaulted to the 90-100 range.
    @commands.command()
    async def gay(self, ctx, *, user=None):     # optionally passes in a user argument
        if user:
            gayness = random.randint(0, 100)
            embed = discord.Embed(description=f'**{user}** is ==> **{gayness}%** gay', color=11342935)
            await ctx.channel.send(embed=embed)
        else:
            if ctx.author.id == 352964311423123458 or ctx.author.id == 194902708535164934:
                gayness = random.randint(90, 100)
            elif ctx.author.id == 216683868244148225:
                gayness = random.randint(100, 200)
            else:
                gayness = random.randint(0, 100)
            embed = discord.Embed(description=f'**{ctx.author.name}** is ==> **{gayness}%** gay', color=11342935)
            await ctx.channel.send(embed=embed)

    # Returns the phrase "Shut the fuck up Baraboomba" along with a silenced seagull
    @commands.command()
    async def baraboomba(self, ctx):
        await ctx.channel.send("Shut the fuck up baraboomba https://imgur.com/a/S0l1n2P")


# Give main bot all commands in this file
def setup(bot):
    bot.add_cog(Messaging(bot))

