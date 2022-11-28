from discord.ext import commands

class YourClassName(commands.Cog):
    #executes with class is initialized
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       await print("Binary Conversion Online")

   
    # takes a number as an argument and sends a message back with the number in binary
    @commands.command()
    async def hello_world(self, ctx, string:str):
        await print("Hello, world!")

async def setup(bot):
    await bot.add_cog(YourClassName(bot))        
     
