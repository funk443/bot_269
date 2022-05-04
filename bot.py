import discord
import os
from discord.ext import commands

intents = discord.Intents.default ()
intents.members = True
activity = discord.Game (name = "GNU Emacs")

f = open ("./TOKEN", "r")
TOKEN = f.read ()
f.close ()

bot = commands.Bot (command_prefix = "a269 ", intents = intents, activity = activity)

@bot.event
async def on_ready ():
  print ("Up")

@bot.command ()
async def license (ctx):
  embed=discord.Embed(title="License", url="https://www.gnu.org/licenses/gpl-3.0.html", description="GNU GPL v3")
  await ctx.send(embed=embed)

for fn in os.listdir ("./cmds"):
  if (fn.endswith (".py")):
    bot.load_extension (f"cmds.{fn[:-3]}")

if (__name__ == "__main__"):
  bot.run(str (TOKEN))
