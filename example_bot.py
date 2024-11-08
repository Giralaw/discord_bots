# This example requires the 'message_content' intent.

import discord
import logging

# disable spammy events
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# enable logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# Get bot token
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

client.run(TOKEN,log_handler=handler, log_level = logging.DEBUG)