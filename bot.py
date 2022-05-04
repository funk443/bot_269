import discord
import json
import os
from discord.ext import commands

intents = discord.Intents.default ()
intents.members = True
intents.guilds = True
activity = discord.Game (name = "GNU Emacs")

f = open ("./TOKEN", "r")
TOKEN = f.read ()
f.close ()

f = open ("config.json", "r")
conf = json.load (f)
f.close ()

bot = commands.Bot (command_prefix = conf["prefix"], intents = intents, activity = activity, help_command = None)

@bot.event
async def on_ready ():
  print ("Up")

@bot.command ()
async def license (ctx):
  embed=discord.Embed(title="License", url="https://www.gnu.org/licenses/gpl-3.0.html", description="GNU GPL v3")
  await ctx.send(embed=embed)

# @bot.command ()
# async def pf (ctx, npf = None):
#   if (npf != None):
#     conf["prefix"] = f"{npf} "
#     f = open ("config.json", "w")
#     json.dump (conf, f)
#     f.close ()
#     await ctx.send (f"Prefix changed to {npf}")
#   else:
#     await ctx.send ("沒給我東西是要怎麼改啦")


for fn in os.listdir ("./cmds"):
  if (fn.endswith (".py")):
    bot.load_extension (f"cmds.{fn[:-3]}")

if (__name__ == "__main__"):
  bot.run(str (TOKEN))
