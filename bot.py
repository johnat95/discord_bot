import asyncio
import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

#get app working directory and append env file name
env_path =  os.path.abspath(os.path.dirname(__file__) + "/bot.env")

#load enviroment variables
load_dotenv(env_path)

#get bot token
token = str(os.getenv("TOKEN"))

#location of cog classes
cogs_dir = './cogs/'

#command prefix, 
prefix = "$"

intent = discord.Intents.default()

bot = commands.Bot(intents=intent, command_prefix=prefix)

async def load_ext():
    for file in os.listdir(cogs_dir):

        if (file.endswith('.py')):

            await bot.load_extension(F'cogs.{file[:-3]}')
            print("Loading " + file)


async def main():
    print("Loading Extensions...")

    await load_ext()
    try:
        await bot.start(token)
        
    except discord.HTTPException as ex:
        print(repr(ex))


asyncio.run(main())


