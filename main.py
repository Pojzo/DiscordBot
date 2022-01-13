import discord
from discord_token import token
import glob
import numpy as np
import random
import cv2

images_people = ["gazdik", "pojzo", "marek", "david"]

client = discord.Client()

def get_images(name: str) -> np.array:
    images = []
    return [filename for filename in glob.glob(f'images/{name}/*.jpg')]

    image = cv2.imread(filename)
    images.append(image)


    return images

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith("!"):
        return
    msg = message.content[1:]
    split_message = msg.split()
    if len(split_message) == 1:
        message.channel.send("Zly command brasko")
        return

    first, second = split_message
    second = second.lower()
    if first == "image":
        if second in images_people:
            images = get_images(second)
            # print(images)
            image = random.choice(images)
            print(image)
            await message.channel.send(file = discord.File(random.choice(images)))


client.run(token)
