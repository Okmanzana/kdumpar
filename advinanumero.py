
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
                     
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    elif message.content.startswith('$guess'):
                gues = message.content
                guess = gues.split(": ")[1]
    
                answer = random.randint(1, 10)      

    
                if int(guess) == answer:
                    await message.channel.send('Correcto!')
                else:
                    await message.channel.send(f'Nope! En realidad es: {answer}.')
    
