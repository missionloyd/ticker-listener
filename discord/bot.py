import os
import discord, time
from discord.ext import commands, tasks
from dotenv import load_dotenv
from whattomine_listener import coin_rankings
from genesis_listener import genesis_status, check_ping
from affirmations_listener import affirmation

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
channel_id = os.getenv('CHANNEL_ID')
client = commands.Bot(command_prefix='!')

@tasks.loop(hours=1)
async def wmine():
    channel = await client.fetch_channel(channel_id)
    await channel.send(coin_rankings(3))

@tasks.loop(hours=0.5)
async def genesis():
    my_id = "520856458414522378"
    channel = await client.fetch_channel(channel_id)
    coa, wrapped_message = check_ping(genesis_status())

    if(coa == 'ping'):
        await channel.send(f"<@{my_id}> {wrapped_message}")
    else:
        await channel.send(wrapped_message)

@tasks.loop(hours=0.45)
async def affirmations():
    channel = await client.fetch_channel(channel_id)
    await channel.send(affirmation())

@client.command()
async def what(ctx):
    channel = await client.fetch_channel(channel_id)
    await channel.send(coin_rankings(3))

@client.command()
async def gene(ctx):
    my_id = "520856458414522378"
    channel = await client.fetch_channel(channel_id)
    coa, wrapped_message = check_ping(genesis_status())

    if(coa == 'ping'):
        await channel.send(f"<@{my_id}> {wrapped_message}")
    else:
        await channel.send(wrapped_message)

@client.command()
async def aff(ctx):
    channel = await client.fetch_channel(channel_id)
    await channel.send(affirmation())

@client.command()
async def man(ctx):
    channel = await client.fetch_channel(channel_id)
    await channel.send('Mining Rankings:\t!what\nGenesis Stats:\t\t!gene\nAffirmation:\t\t\t!aff')

@client.command()
async def hello(ctx):
    await ctx.send(f"hello, {ctx.author.mention}")

@client.event
async def my_id(message):
    print(message.author.id)


@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')

@client.event
async def logout():
    await client.logout()

wmine.start()
genesis.start()
affirmations.start()
client.run(TOKEN)