#programmer: Nathan Johnston

#purpose start a bot that automatice detects new cog class files in thge ./cog folders.


import asyncio
import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

#get app working directory and append env file name
env_path =  os.path.abspath(os.path.dirname(__file__) + "/bot.env")

#load enviroment variables
load_dotenv(env_path)

#get bot token from envroment
token = str(os.getenv("TOKEN"))

#location of cog classes
cogs_dir = './cogs/'

#command prefix 
prefix = "$"

intent = discord.Intents.default()

bot = commands.Bot(intents=intent, command_prefix=prefix)

async def load_ext():
    """get a list of the files in the ./cog folder, these files each contain a class which inherits
    the commands.Cog class. These classes contain collections of methods decorated with @commands.command,
    which can be called from a direct message to the bot, leading with the command prefix.

    ie. $method_name args
    """ 

    for file in os.listdir(cogs_dir):

        if (file.endswith('.py')):

            #load file if its a python file
            await bot.load_extension(F'cogs.{file[:-3]}')
            print("Loading " + file)


async def main():
    print("Loading Extensions...")

    await load_ext()
    try:
        await bot.start(token)
        
    except discord.HTTPException as ex:
        #prints a string representing the error
        print(repr(ex))


asyncio.run(main())


