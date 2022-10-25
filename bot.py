import asyncio
import discord
from discord.ext import commands
import os
import json

cogs_dir = './cogs/'

prefix = "$"

intent = discord.Intents.default()

bot = commands.Bot(intents=intent, command_prefix=prefix)


async def load_ext():
    for file in os.listdir(cogs_dir):

        if (file.endswith('.py')):

            await bot.load_extension(F'cogs.{file[:-3]}')
            print(file[:-3])


async def main():
    print("loading exts")

    await load_ext()


asyncio.run(main())
