import discord
from discord_token import token

images_people = ["gazdik", "pojzo", "marek", "david"]
images = {"gazdik" : }

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.startswith("!"):
        return
    message = message[1:]
    split_message = message.split()
    if len(split_message) == 1:
        message.channel.send("Zly command brasko")
        return

    first, second = split_message
    if first == "image":
        if tolower(second) in images_people:



client.run(token)
