import discord
from discord.ext import commands,tasks
import random
from datetime import *

description = '''A bot to remind your friends birthday.'''
intents = discord.Intents.default()
intents.members = True
birthday = {}
today = date.today()

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def diane(ctx):
    if ctx.message.author.id == 304669210770931712:
        await ctx.send("SOUMA SOUMA SOUMA! \nSOUMA SOUMA SOUMA!")
    else:
        await ctx.send("Je suis Diane! Le serpent de l'envie! :wave:")
                       
@bot.command()
async def king(ctx):
    file = discord.File("diane_and_king.jpg",filename="love.jpg")
    await ctx.send("king :smiling_face_with_3_hearts:",file=file)
    
@bot.command()
async def add(ctx, name: str, birth: str):
    role = ctx.guild.get_role(928728017428180992)
    if role in ctx.author.roles:
        await ctx.send("Tu n'as pas la permission de me donner des ordres ! :angry:")
        print(birthday)
    else:
        birthday.update({name:birth})
        await ctx.send("Oh ! Un nouvel ami !")
        print(birthday)
        
@bot.command()
async def delete(ctx, name: str):
    if birthday.pop(name, None):
        await ctx.send("Gowther ! Effacement de mémoire !")
    else:
        await ctx.send("Gowther ? Tu m'as déja effacé la mémoire?")
    print(birthday)

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(928388039435227229)
    for nom, date in birthday.items():
        if(today.strftime("%d/%m") == date):
            await message_channel.send("Otanjobi omedeto gozaimasu %s :partying_face: \nNous te souhaitons un joyeux anniversaire, profites bien de ta journée :tada: \nMerci d'être parmi nous ici!:smiling_face_with_3_hearts:" % (nom))
            continue
        return
@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")
    
called_once_a_day.start()
bot.run('OTI4MzY2OTUzNjMzMDIxOTYy.YdXvGQ.0P2lMhnfrP5ul9LVGDSMlw5q2WU')
