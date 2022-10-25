import discord
from discord.ext import commands


class BinaryConverter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Ready")


async def setup(bot):
    await bot.add_cog(BinaryConverter(bot))