import discord
from discord.ext import commands

intents = discord.Intents.default ()
intents.members = True

bot = commands.Bot (command_prefix = "a269 ", intents = intents)

@bot.event
async def on_ready ():
  print ("Up")

@bot.event
async def on_message (message):
  if (message.author == bot.user):
    return

  if ("linux" in message.content.lower ().split ()):
    await message.channel.send ("I'd just like to interject for a moment")

@bot.event
async def on_message_edit (before, after):
  if (before.author == bot.user):
    return

  await before.channel.send (f"改三小")

@bot.command ()
async def test (ctx):
  await ctx.send ("ABC")

bot.run("OTY3OTE0OTk1NTA3NjU4Nzcy.YmXPFQ.q-yNgGqf_D9Mc_wTbWcAOBOfgtA")
