import discord
from discord.ext import commands
import os, asyncio
import logging
import logging.handlers
from pathlib import Path


from help_cog import help_cog
from music_cog import music_cog

# set up output logging
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

bot.remove_command("help")

# Use Path to get current script's directory
current_dir = Path(__file__).parent
token_file_path = current_dir / '../token.txt'

log_file_path = current_dir/ 'discord.log'
with open(token_file_path, 'r') as file:
    TOKEN = file.read().strip()

async def main():

    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename=log_file_path,
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)

asyncio.run(main())
