from autocorrect import Speller
from discord.ext import commands
from gingerit.gingerit import GingerIt

spell = Speller(fast=True)
caps = GingerIt()

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
        if "?" not in array[len(array) - 1] and "!" not in array[len(array) - 1] and "." not in array[len(array) - 1]:
            array[len(array) - 1] = array[len(array) - 1] + "."
        autocorrectMsg = " ".join(array)
        newMsg = caps.parse(autocorrectMsg)["result"]
        print("---------")
        print("Old: " + message.content + "\nNew: " + newMsg)
        await message.edit(content=newMsg)

bot.run(token, bot=False)