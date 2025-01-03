import discord 
from discord.ext import commands
import os
import webserver
import random
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def suma(ctx,n1:int,n2:int):
    """Esta función suma dos números enteros y devuelve el resultado."""
    resultado = n1 + n2
    await ctx.send(f"La suma de {n1} y {n2} es {resultado}")
@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)
@bot.command()
async def resta(ctx,n1:int,n2:int):
    """Esta función suma dos números enteros y devuelve el resultado."""
    resultado1 = n1 - n2
    await ctx.send(f"La resta de {n1} y {n2} es {resultado1}")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)
