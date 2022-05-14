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
import random
from discord.ext import commands
from core.classes import cog_ext

class reply (cog_ext):
  @commands.command ()
  async def reply (self, ctx, key, content_1 = None, content_2 = None):
    if (f"data_reply_{ctx.guild.id}.json" not in os.listdir ("./datas/reply")):
      f = open (f"./datas/reply/data_reply_{ctx.guild.id}.json", "w")
      json.dump ({}, f)
      f.close ()

    f = open (f"./datas/reply/data_reply_{ctx.guild.id}.json", "r")
    data = json.load (f)
    f.close ()

    if (key == "add"):
      if (content_1 == None):
        await ctx.send ("你是要我加什麼啦")
      elif (len (ctx.message.attachments) != 0):
        f = open (f"./datas/reply/data_reply_{ctx.guild.id}.json", "w")
        urls = []
        for i in ctx.message.attachments:
          urls.append (i.url)

        data[str (content_1)] = urls
        json.dump (data, f)
        f.close ()
        await ctx.send (f"加入了 {content_1}")
      elif (content_2 == None):
        await ctx.send ("你是要我加什麼啦")
      else:
        f = open (f"./datas/reply/data_reply_{ctx.guild.id}.json", "w")
        data[str (content_1)] = str (content_2)
        json.dump (data, f)
        f.close ()

        await ctx.send (f"以後有人傳{content_1}，我會回{content_2}")

    elif (key == "del"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我是要刪什麼啦")
      else:
        if (content_1 in data):
          f = open (f"./datas/reply/data_reply_{ctx.guild.id}.json", "w")
          data.pop (content_1)
          json.dump (data, f)
          f.close ()
          await ctx.send (f"刪除了 {content_1}")
        else:
          await ctx.send ("先生，沒有那種東西")

    elif (key == "findk"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我是要怎麼找啦")
      else:
        keys = []
        for k, v in data.items ():
          if (content_1 in v):
            keys.append (k)

        for i in keys:
          data_list = data[i]
          await ctx.send (f"{i}: {data_list}")

    elif (key == "findv"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我是要怎麼找啦")
      else:
        keys = []
        for k, v in data.items ():
          if (content_1 in k):
            keys.append (k)

        for i in keys:
          data_list = data[i]
          await ctx.send (f"{i}: {data_list}") 
                             
    elif (key == "list"):
      if (len (data) != 0):
        for i in data:
          await ctx.send (f"`{i}:{data[i]}`")
      else:
        await ctx.send ("竟然一個東西都沒有")
          
    else:
      await ctx.reply ("你好像打錯東西囉")

def setup (bot):
  bot.add_cog (reply (bot))
