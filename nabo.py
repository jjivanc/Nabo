import discord
from discord.ext import commands
import os
#import io
import aiohttp
from bs4 import BeautifulSoup
#import webscraping
from webscraping import link_s
#import random

#Teste_s = teste_

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game(name="Ativo .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"Você é {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@client.command()
async def s(ctx):
  for resposta in link_s():
    await ctx.send(resposta)

#@client.command(name="img")
#async def imagen(ctx,*,text):
#	message = ctx.message 
#	await message.delete()
#	##await ctx.send(f"https://t.nhentai.net/galleries/{text}/cover.jpg")

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://nhentai/r/g/345687') as r:
            res = await r.json()
            embed.set_image(url=res['u0022:363854'])
            await ctx.send(embed=embed)

@client.command(name='teste')
async def imagen(ctx,*,text):
    sess = aiohttp.ClientSession()
    req = await sess.get('https://nhentai.net/g/{text}')

    #soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(await req.read(), 'html.parser')
    link = soup.find_all(class_='lazyload',)['src']


    await ctx.send(link)

client.run(token)