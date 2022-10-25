#programmer: Nathan Johnston

#purpose: converts numbers to binary, with the option of breaking down the math at each bit

from discord.ext import commands


class BinaryConverter(commands.Cog):

    docs = """The int_binary method is called by sending "$int_binary num" where
        num is a positive integer in a direct message to the bot,
        the number is converted into binary, which is sent back in a message
        Does not contain leading zeros.

        #Example: "$int_binary 234" sends 11101010
        #Example: "$int_binary 1" sends 1


        int_binary_breakdown is called by sending "$int_binary_breakdown num" where
        num is a integer in a direct message to the bot, 
        the number is converted into binary, which is sent back in a message, along with the
        equation for each bit. Does not contain leading zeros.

        #Example: "$int_binary_breakdown 10" sends:

        10 represented in binary is 1010,
        and breaks down from left to right like so:

        bit 3 adds 8
        equation: 2 to the power of 3
        running total: 8

        bit 2 adds nothing
        running total: 8 

        bit 1 adds 2
        equation: 2 to the power of 1
        running total: 10

        bit 0 adds nothing
        running total: 10 """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       await print("Binary Conversion Online")

    @commands.command()
    async def docu(self, ctx):
       await ctx.send(self.docs)

   
    # takes a number as an argument and sends a message back with the number in binary
    @commands.command()
    async def int_binary(self, ctx, string:str):

        try:
            #convert string to int
            num = int(string)

            if(num < 1):
                await ctx.send("Ack! I need positive number greater than zero!")
                return

            #convert int to binary, slice first 2 digits, 0b
            binary = bin(num)[2:]

            #convert back to string
            binary_string = str(binary)

            #send message
            await ctx.send(binary_string)

         #catch value error if num_string cannot be coverted into a number    
        except ValueError as ex:
            await ctx.send(repr(ex)+"\nOh dear, that's not a number!")

    @commands.command()
    async def int_binary_breakdown(self, ctx, num_string:str):

        try:
        
            #convert string to int
            num = int(num_string)

            if(num < 1):
                await ctx.send("Ack! I need positive number greater than zero!")
                return


            #convert int to binary, slice first 2 digits, 0b
            binary = bin(num)[2:]

            #convert back to string
            binary_string = str(binary)

            #keeps track of proper power for base two, reserch binary for more information
            n = len(binary_string)-1

            #track running total of bits read right to left
            running_total = 0 

            # intialize temp value variable outside of loop
            value = 0 

            #Starting output string
            output_string = num_string + " represented in binary is " + binary_string
            output_string += ",\nand breaks down from left to right like so:\n\n"

            for char in binary_string:

                #if bit is one, calulate value of bit
                if(char == '1'):
                
                   #calculate value of bit
                    value = 2**n

                    #add value to total
                    running_total += value

                    #add bit information to output string
                    output_string += f"bit {n} adds {value}"
                    output_string +=  f"\nequation: 2 to the power of {n}"
                    output_string +=  f"\nrunning total: {running_total}\n\n"


                else:
                    output_string += f"bit {n} adds nothing\n"
                    output_string += f"running total: {running_total} \n\n"


                #decrement n
                n -= 1 

                #if adding another set of bit data will surpass the character limit
                #send the string and set it empty to allow more dataS
                if(len(output_string) > 1924):
                    await ctx.send(output_string)

                    output_string = ""

            #send message
            await ctx.send(output_string)
        #catch value error if num_string cannot be coverted into a number    
        except ValueError as ex:
            await ctx.send(repr(ex)+"\nOh dear, that's not a number!")

async def setup(bot):
    await bot.add_cog(BinaryConverter(bot))        
     
