"""
  Copyright (C) 2022 CToID

  This file is part of bot_269.

  bot_269 is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

  bot_269 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License along with bot_269. If not, see <https://www.gnu.org/licenses/agpl-3.0.html>.
"""
import discord
import json
import os
from discord.ext import commands

intents = discord.Intents.default ()
intents.members = True
activity = discord.Game (name = "GNU Emacs")

f = open ("./TOKEN", "r")
TOKEN = f.read ()
f.close ()

f = open ("config.json", "r")
conf = json.load (f)
f.close ()

f = open ("prefixes.json", "r")
pfs = json.load (f)
f.close ()
# print (twitch_names)
# print (twitch_chan)
# print (twitch_stat)
# print (twitch_content)
# print (twitch_emd)

async def get_prefix (bot, ctx):
  if (str (ctx.guild.id) not in pfs):
    return pfs["default"]
  else:
    return pfs[str (ctx.guild.id)]

bot = commands.Bot (command_prefix = get_prefix, intents = intents, activity = activity, help_command = None)

@bot.event
async def on_ready ():
  print ("Up")

@bot.command ()
async def change_prefix (ctx, npf = None):
  if (npf != None):
    pfs[str (ctx.guild.id)] = npf
    await ctx.send (f"Prefix changed to {npf}")
  else:
    pfs[str (ctx.guild.id)] = "a269 "
    await ctx.send ("沒給我東西那我就把他改回預設的了")

  f = open ("prefixes.json", "w")
  json.dump (pfs, f)
  f.close ()

for fn in os.listdir ("./cmds"):
  if (fn.endswith (".py")):
    bot.load_extension (f"cmds.{fn[:-3]}")

if (__name__ == "__main__"):
  bot.run(str (TOKEN))

