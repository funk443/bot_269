"""
Copyright (C) 2022 CToID

  This file is part of bot_269.

  bot_269 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

  bot_269 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
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

    if ((message.author.id == 159985870458322944) and (message.author.bot == True)
        and ("484要制裁一下" in message.content)):
      await message.reply ("閉嘴好不好")

    if (f"data_reply_{message.guild.id}.json" not in os.listdir ("./datas")):
      return

    f = open (f"./datas/data_reply_{message.guild.id}.json")
    data = json.load (f)
    f.close ()

    if (message.content in data):
      if (type (data[message.content]) == list):
        for i in data[message.content]:
          await message.channel.send (i)
      else:
        await message.channel.send (data[message.content])

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

def setup (bot):
  bot.add_cog (events (bot))
