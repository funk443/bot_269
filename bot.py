import discord
from discord.ext import commands
import json

with open ("config.json", mode = "r", encoding = "utf8") as conf:
  conf_data = json.load (conf)

intents = discord.Intents.default ()
intents.members = True

bot = commands.Bot (command_prefix = "a269 ", intents = intents)

@bot.event
async def on_ready ():
  print ("Hello, World!")

@bot.event
async def on_member_join (member):
  print (f"{member} joined!")
  channel = bot.get_channel (int(conf_data["general"]))
  await channel.send (f"{member} joined!")
  
@bot.event
async def on_member_remove (member):
  print (f"{member} left!")
  channel = bot.get_channel (int(conf_data["general"]))
  await channel.send (f"{member} left!")

@bot.command ()
async def ping (ctx):
  await ctx.send (f"{round (bot.latency * 1000)} ms")

bot.run (conf_data["TOKEN"])

