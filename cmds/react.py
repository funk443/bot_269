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

class reaction (cog_ext):
  @commands.command ()
  async def react (self, ctx, key, content_1 = None, *content_2):
    if (f"data_react_{ctx.guild.id}.json" not in os.listdir ("./datas/react")):
      f = open (f"./datas/react/data_react_{ctx.guild.id}.json", "w", encoding = "utf-8")
      json.dump ({}, f)
      f.close ()

    f = open (f"./datas/react/data_react_{ctx.guild.id}.json", "r", encoding = "utf-8")
    reacts = json.load (f)
    f.close ()

    if (key == "add"):
      if ((content_1 == None) or (len (content_2) == 0)):
        await ctx.send ("你沒給我東西我要怎麼加")
      else:
        f = open (f"./datas/react/data_react_{ctx.guild.id}.json", "w", encoding = "utf-8")
        reacts[content_1] = content_2
        json.dump (reacts, f)
        f.close ()
        await ctx.send (f"以後看到{content_1}，我會按{content_2}")
        
    elif (key == "del"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我要怎麼刪")
      elif (content_1 not in reacts):
        await ctx.send (f"先生，這裡沒有{content_1}")
      else:
        f = open (f"./datas/react/data_react_{ctx.guild.id}.json", "w", encoding = "utf-8")
        reacts.pop(content_1)
        json.dump (reacts, f)
        f.close ()
        await ctx.send (f"掰掰{content_1}")

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
      if (len (reacts) != 0):
        for i in reacts:
          await ctx.send (f"```{i}:{reacts[i]}```")
      else:
        await ctx.send ("竟然一個東西都沒有")

    else:
      ctx.send ("你是不是打錯了什麼東西")
    
def setup (bot):
  bot.add_cog (reaction (bot))
