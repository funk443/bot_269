import discord
from discord.ext import commands
import json
import random
import os

with open ("config.json", mode = "r", encoding = "utf8") as conf:
  conf_data = json.load (conf)

intents = discord.Intents.default ()
intents.members = True

bot = commands.Bot (command_prefix = "a269 ", intents = intents)

@bot.event
async def on_ready ():
  print ("Hello, World!")

@bot.command ()
async def load (ctx, extension):
  bot.load_extension (f"cmds.{extension}")
  await ctx.send (f"{extension} Loaded")

@bot.command ()
async def unload (ctx, extension):
  bot.unload_extension (f"cmds.{extension}")
  await ctx.send (f"{extension} Unloaded")

@bot.command ()
async def reload (ctx, extension):
  bot.reload_extension (f"cmds.{extension}")
  await ctx.send (f"{extension} Reloaded")

for filename in os.listdir ("./cmds"):
  if (filename.endswith (".py")):
    bot.load_extension(f"cmds.{filename[:-3]}")
    
if __name__ == "__main__":
  bot.run (conf_data["TOKEN"])

