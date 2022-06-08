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

class what_to_eat (cog_ext):
  @commands.command ()
  async def 吃什麼 (self, ctx, *option):
    option = list (option)
    if (f"data_food_{ctx.guild.id}.json" not in os.listdir ("./datas/food")):
      f = open (f"./datas/food/data_food_{ctx.guild.id}.json", "w", encoding = "utf-8")
      json.dump ({"food":[]}, f)
      f.close ()

    f = open (f"./datas/food/data_food_{ctx.guild.id}.json", "r", encoding = "utf-8")
    food = json.load (f)
    f.close ()

    if ("add" in option):
      if (len (option) == 1):
        await ctx.send ("你沒說要加什麼R")
      else:
        f = open (f"./datas/food/data_food_{ctx.guild.id}.json", "w", encoding = "utf-8")
        
        for i in option[1:]:
          food["food"].append (i)
          
        json.dump (food, f)
        f.close ()
    elif ("del" in option):
      if (len (option) == 1):
        await ctx.send ("你沒說要移除什麼R")
      else:
        f = open (f"./datas/food/data_food_{ctx.guild.id}.json", "w", encoding = "utf-8")
        for i in option[1:]:
          if (i not in food["food"]):
            await ctx.send (f"先生，沒有{i}")
          else:
            food["food"].remove (i)
        json.dump (food, f)
        f.close ()
    elif ("clr" in option):
      f = open (f"./datas/food/data_food_{ctx.guild.id}.json", "w", encoding = "utf-8")
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
  bot.add_cog (what_to_eat (bot))
