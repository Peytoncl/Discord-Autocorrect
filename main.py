from autocorrect import Speller
from discord.ext import commands

spell = Speller(fast=True)

bot = commands.Bot(command_prefix="", self_bot=True)
token = input("Your Discord token: ")

@bot.event
async def on_ready():
    print("You're good to go!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        array = message.content.split()
        for x in array:
            array[array.index(x)] = spell(x)
        newMsg = " ".join(array)
        await message.edit(content=newMsg)

bot.run(token, bot=False)