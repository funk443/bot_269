"""
Copyright (C) 2022 CToID

  This file is part of bot_269.

  bot_269 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

  bot_269 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import json
import os
from discord.ext import commands

intents = discord.Intents.default ()
intents.members = True
intents.guilds = True
import discord
import json
import os
import random
from discord.ext import commands
from core.classes import cog_ext

js = open ("config.json")
conf = json.load (js)
js.close ()

class cmd (cog_ext):
  @commands.command ()
  async def reply (self, ctx, key, content_1 = None, content_2 = None):
    if (f"data_reply_{ctx.guild.id}.json" not in os.listdir ("./datas")):
      f = open (f"./datas/data_reply_{ctx.guild.id}.json", "w")
      json.dump ({}, f)
      f.close ()

    f = open (f"./datas/data_reply_{ctx.guild.id}.json", "r")
    data = json.load (f)
    f.close ()

    if (key == "add"):
      if (content_1 == None):
        await ctx.send ("你是要我加什麼啦")
      elif (len (ctx.message.attachments) != 0):
        f = open (f"./datas/data_reply_{ctx.guild.id}.json", "w")
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
        f = open (f"./datas/data_reply_{ctx.guild.id}.json", "w")
        data[str (content_1)] = str (content_2)
        json.dump (data, f)
        f.close ()

        await ctx.send (f"加入了 {content_1}")

    elif (key == "del"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我是要刪什麼啦")
      else:
        if (content_1 in data):
          f = open (f"./datas/data_reply_{ctx.guild.id}.json", "w")
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
          await ctx.send (f"```{i}:{data[i]}```")
      else:
        await ctx.send ("竟然一個東西都沒有")
          
    else:
      await ctx.reply ("你好像打錯東西囉")

  @commands.command ()
  async def 吃什麼 (self, ctx, *option):
    option = list (option)
    if (f"data_food_{ctx.guild.id}.json" not in os.listdir ("./datas")):
      f = open (f"./datas/data_food_{ctx.guild.id}.json", "w")
      json.dump ({"food":[]}, f)
      f.close ()

    f = open (f"./datas/data_food_{ctx.guild.id}.json", "r")
    food = json.load (f)
    f.close ()

    if ("add" in option):
      if (len (option) == 1):
        await ctx.send ("你沒說要加什麼R")
      else:
        f = open (f"./datas/data_food_{ctx.guild.id}.json", "w")
        
        for i in option[1:]:
          food["food"].append (i)
          
        json.dump (food, f)
        f.close ()
    elif ("del" in option):
      if (len (option) == 1):
        await ctx.send ("你沒說要移除什麼R")
      else:
        f = open (f"./datas/data_food_{ctx.guild.id}.json", "w")
        for i in option[1:]:
          if (i not in food["food"]):
            await ctx.send (f"先生，沒有{i}")
          else:
            food["food"].remove (i)
        json.dump (food, f)
        f.close ()
    elif ("clr" in option):
      f = open (f"./datas/data_food_{ctx.guild.id}.json", "w")
      json.dump ({"food":[]}, f)
      f.close ()
    elif ("list" in option):
      food_list = food["food"]

      await ctx.send (food_list)
    elif (option == []):
      food_option = food["food"]
      if (len (food_option) == 0):
        await ctx.send ("預設清單是空的我要怎麼選啦，用```a269 吃什麼 add```來加入食物")
      else:
        await ctx.send (f"沒有給選項，我會從 [{', '.join (food_option)}] 裡選。吃 {random.choice (food_option)} 好了")
    else:
      await ctx.send (f"吃 {random.choice (option)} 好了")
      
    
def setup (bot):
  bot.add_cog (cmd (bot))
