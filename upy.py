import discord
from discord.ext import commands
from datetime import datetime
import asyncio

TOKEN = 'NzEzODQ1OTc3NTg0MjM4NjMz.XsmDGQ.WuVtvv9uT0uPFaZHJGVhPGyKI3E'

bot = commands.Bot(command_prefix='!') #инициализируем бота с префиксом '!'

@bot.command(pass_context=True) 
async def members(ctx, message):
    for guild in bot.guilds:
      for member in guild.members:
        await ctx.send(member)

@bot.command(pass_context=True) 
async def ping(ctx, message):
    
    message = (message.replace(".", "_")).split("_")
    
    str = [int(message[i]) for i in range(3)]

    hour = int(message[-2])

    minute = int(message[-1])
    
    message = message[3:]
    
    date = datetime(str[2], str[1], str[0], hour, minute) - datetime.now()
    
    date = round(date.total_seconds())

    print( datetime.now())

    print(date)
    
    await asyncio.sleep(date)
    
    await ctx.send("Твое задание:" + " ".join(message[:-2]) + " Время: " + "".join(message[-2]) + ":" + "".join(message[-1]) )
                
bot.run(TOKEN)

