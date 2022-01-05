import discord
from discord_token import token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ano?'):
        await message.channel.send('nieeeeee!')

    if message.content.startswith('o7'):
        await message.channel.send('o7')

    if message.content.startswith('o/'):
        await message.channel.send('\o')

    if message.content.startswith('\o'):
        await message.channel.send('o/')
client.run(token)
