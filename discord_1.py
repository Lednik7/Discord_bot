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

        if message in tasks:
            pass
        
        else:
            tasks.append(message)

        await ctx.send("ID Вашего задания: " + str(tasks.index(message)))

    elif message.content.startswith('!see'):
        try:
            ctx = message.channel

            await ctx.send("\n".join(tasks))
            
        except:
            
            await ctx.send("Список пуст, заполните его")
        
    elif message.content.startswith('!members'):

        ctx = message.channel
            
        for guild in bot.guilds:     
            for member in guild.members:
                await ctx.send(member)

    elif message.content.startswith('!clear'):
        
        ctx = message.channel
        
        tasks.clear()
        
        await ctx.send("Список очищен")

    elif message.content.startswith('!del'):
        
        try:
        
            ctx = message.channel

            message = (message.content)[5:]

            number = message.replace(" ", "")

            del tasks[int(number)]

            await ctx.send("Удален элемент " + number)

        except:

            await ctx.send("Возможно, элемента в списке нет")

    elif message.content.startswith('!ping'):

        try:
            ctx = message.channel

            message = ((message.content).replace(".", " ")).replace(":", " ")

            message = message.split()[1:] #24 5 2020 17 46 1 @PopularDwarf
            
            date = [int(message[i]) for i in range(3)] #24 5 2020 17 46 1 @PopularDwarf 

            hour = int(message[3]) #17

            minute = int(message[4]) #46

            id = int(message[5]) #0
                
            message = message[6:] #@PopularDwarf 

            offset = datetime.timezone(datetime.timedelta(hours=3))
                
            date = datetime.datetime(date[2], date[1], date[0], hour, minute) - (datetime.datetime.now(offset)).replace(tzinfo=None)
                
            date = round(date.total_seconds())

            print( datetime.datetime.now(offset))

            print(date)
                
            await asyncio.sleep(date)

            await ctx.send("Тебе задание: " + " ".join(message) + ": "+ str(tasks[id]) + "\nВремя: " + str(hour)+ ":" + str(minute) )
            
        except:

            await ctx.send("Что-то пошло не так")
            
bot.run(TOKEN)
