from discord.ext import commands
from constants import TOKEN

bot = commands.Bot(command_prefix="z!")


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    ##########
    # bruh   #
    ##########

    if "bruh moment" in message.content:
        await message.channel.send("bruh moment indeed")
    elif "bruh" in message.content:
        await message.channel.send("bruh")
    elif "hurb" in message.content:
        await message.channel.send("hurb")


bot.run(TOKEN)
