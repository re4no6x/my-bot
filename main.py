import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Khdam: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content.lower()
    if "salam" in msg or "slm" in msg:
        await message.channel.send("Salam a sat! Kidayr? 👋")
    if "kidayr" in msg:
        await message.channel.send("Ana mzyan, nta kidayr? 😎")
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Ana hna 🏓")

bot.run(os.environ.get("TOKEN"))
