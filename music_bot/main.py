import discord
from discord.ext import commands
import os, asyncio
import logging

from help_cog import help_cog
from music_cog import music_cog

# set up output logging
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

bot.remove_command("help")


async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(os.getenv('TOKEN'))

asyncio.run(main())