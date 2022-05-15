"""
Copyright (C) 2022 CToID

  This file is part of bot_269.

  bot_269 is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

  bot_269 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License along with bot_269. If not, see <https://www.gnu.org/licenses/agpl-3.0.html>.
"""
import discord
import json
import random
import os
from discord.ext import commands
from core.classes import cog_ext

js = open ("config.json")
conf = json.load (js)
js.close ()

class events (cog_ext):
  # @commands.Cog.listener ()
  # async def on_member_join (self, member):
  #   channel = self.bot.get_channel (conf["general"])
  #   await channel.send (f"你好R, {member.mention}")

  # @commands.Cog.listener ()
  # async def on_member_leave (self, member):
  #   channel = self.bot.get_channel (conf["general"])
  #   await channel.send (f"一路好走, {member.mention}")
  
  @commands.Cog.listener ()
  async def on_message (self, message):
    if (message.author == self.bot.user):
      return

    if ("PREFIX" == message.content):
      f = open ("prefixes.json", "r")
      pf = json.load (f)
      f.close ()

      try:
        pref = pf[str (message.guild.id)]
      except:
        pref = pf["default"]

      await message.channel.send (f'現在的前綴字是"`{pref}`"')

    if ("LICENSE" == message.content):
      await message.channel.send (file = discord.File ("LICENSE.txt"))

    if ("COPYRIGHT" == message.content):
      f = open ("./resources/license_notice", "r")
      lic = f.read ()
      f.close ()
      await message.channel.send (f"```{lic}```")

    if ("CREDIT" == message.content):
      f = open ("credits.txt", "r")
      credit = f.read ()
      f.close ()

      await message.channel.send (f"`{credit}`")

    if ((message.author.id == 159985870458322944) and (message.author.bot == True)
        and ("484要制裁一下" in message.content)):
      await message.reply ("閉嘴好不好")

    if (f"data_reply_{message.guild.id}.json" not in os.listdir ("./datas/reply")):
      f = open (f"./datas/data_reply_{message.guild.id}.json", "w")
      json.dump ({}, f)
      f.close ()

    if (f"data_react_{message.guild.id}.json" not in os.listdir ("./datas/react")):
      f = open (f"./datas/data_react_{message.guild.id}.json", "w")
      json.dump ({}, f)
      f.close ()

    f = open (f"./datas/reply/data_reply_{message.guild.id}.json")
    data = json.load (f)
    f.close ()

    f = open (f"./datas/react/data_react_{message.guild.id}.json", "r")
    reacts = json.load (f)
    f.close ()

    if ((message.content in data) and (message.author.bot == False)):
      if (type (data[message.content]) == list):
        for i in data[message.content]:
          await message.channel.send (i)
      else:
        await message.channel.send (data[message.content])

    if (message.content in reacts):
      for i in reacts[message.content]:
        await message.add_reaction (i)

    if ("linux" in message.content.lower ().split ()):
      f = open (conf["GNULinux"])
      await message.channel.send (f"```{f.read ()}```")
      f.close ()
  
  # @commands.Cog.listener ()
  # async def on_message_edit (self, before, after):
  #   if (before.author == self.bot.user):
  #     return
  
  #   word = random.choice (conf["kai"])
  #   await before.reply (word)

  @commands.Cog.listener ()
  async def on_command_error (self, ctx, error):
    word = random.choice (conf["wtf"])
    await ctx.reply (f"{word}。這些東西錯了啦: ```{error}```")
    print (error)

def setup (bot):
  bot.add_cog (events (bot))
