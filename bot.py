import discord
from discord.ext import commands

intents = discord.Intents.default ()
intents.members = True

bot = commands.Bot (command_prefix = "269", intents = intents)

@bot.event
async def on_ready ():
  print ("Hello, World!")

@bot.event
async def on_member_join (member):
  print (f"{member} joined!")
  channel = bot.get_channel (967880010281123913)
  await channel.send (f"{member} joined!")
  
@bot.event
async def on_member_remove (member):
  print (f"{member} left!")
  channel = bot.get_channel (967880010281123913)
  await channel.send (f"{member} left!")

bot.run ("OTY3OTE0OTk1NTA3NjU4Nzcy.YmXPFQ.q-yNgGqf_D9Mc_wTbWcAOBOfgtA")

