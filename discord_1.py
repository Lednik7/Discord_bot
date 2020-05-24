import discord
from discord.ext import commands
import datetime
import asyncio

TOKEN = 'NzE0MDg4MTE3NTM1MjQ0MzIw.XspkpA.9VZsc0AqR_GpKULT80hGUFolgr' + 'c'

bot = commands.Bot(command_prefix='!') #инициализируем бота с префиксом '!'

global tasks
tasks = []
        
@bot.event
async def on_message(message):
    
    if message.content.startswith('!task'):

        ctx = message.channel
        
        message = (message.content)[6:]
        
        tasks.append(message)

        await ctx.send("ID Вашего задания: " + str(len(tasks)-1))

    elif message.content.startswith('!see'):

        ctx = message.channel

        await ctx.send("\n".join(tasks))
        
    elif message.content.startswith('!members'):

        ctx = message.channel
            
        for guild in bot.guilds:     
            for member in guild.members:
                
                await ctx.send(member)

    elif message.content.startswith('!ping_task'):
        
        ctx = message.channel
        
        message = ((message.content).split())[1:]
        
        try:
            date = [int(message[i]) for i in range(3)] #день, месяц, год #24 5 2020 @PopularDwarf  0 17 46

            hour = int(message[-2]) #17

            minute = int(message[-1]) #46
            
            message = message[3:] #@PopularDwarf  0 17 46

            id = int(message[-3]) #0
            
            offset = datetime.timezone(datetime.timedelta(hours=3))
            
            date = datetime.datetime(date[2], date[1], date[0], hour, minute) - (datetime.datetime.now(offset)).replace(tzinfo=None)
            
            date = round(date.total_seconds())

            print( datetime.datetime.now(offset))

            print(date)
            
            await asyncio.sleep(date)

            await ctx.send("Тебе задание: " + " ".join(message[:-3]) + " "+ str(tasks[id]) + " Время: " + "".join(message[-2]) + ":" + "".join(message[-1]) )
            
        except:
            
            await ctx.send("Что-то пошло не так. Формат(через пробел): день месяц год id-пользователя номер-таска часы минуты")
            
    elif message.content.startswith('!ping'):
        
        ctx = message.channel
        
        message = ((message.content).split())[1:]

        date = [int(message[i]) for i in range(3)] #день, месяц, год

        hour = int(message[-2])

        minute = int(message[-1])
        
        message = message[3:]
        
        offset = datetime.timezone(datetime.timedelta(hours=3))
        
        date = datetime.datetime(date[2], date[1], date[0], hour, minute) - (datetime.datetime.now(offset)).replace(tzinfo=None)
        
        date = round(date.total_seconds())

        print( datetime.datetime.now(offset))

        print(date)
        
        await asyncio.sleep(date)

        await ctx.send("Тебе сообщение: " + " ".join(message[:-2]) + " Время: " + "".join(message[-2]) + ":" + "".join(message[-1]) )
        
        await ctx.send("ok")
        
        
bot.run(TOKEN)
