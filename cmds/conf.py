"""
Copyright (C) 2022 CToID

  This file is part of bot_269.

  bot_269 is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

  bot_269 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License along with bot_269. If not, see <https://www.gnu.org/licenses/agpl-3.0.html>.
"""
import discord
import os
import json
from discord.ext import commands
from core.classes import cog_ext

class configs (cog_ext):
  @commands.command ()
  async def usr_conf (self, ctx):
    if (f"usr_conf_{ctx.author.id}.json" not in os.listdir("./datas/config/user")):
      f = open (f"./datas/config/user/usr_conf_{ctx.author.id}.json", "w")
      json.dump ({}, f)
      f.close ()
    return

  @commands.command ()
  async def svr_conf (self, ctx, key = None, option = None, ans = None):
    if (f"svr_conf_{ctx.guild.id}.json" not in os.listdir("./datas/config/server")):
      default = open (f"./datas/config/server/default.json", "r")
      f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "w")
      json.dump (json.load (default), f)
      f.close ()

    f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "r")
    confs = json.load (f)
    f.close ()

    if ((f"<@{ctx.author.id}>" in confs["admin"]) or (ctx.author == ctx.guild.owner)):
      if (key == None):
        await ctx.send (confs)
      elif ((option == None) or (ans == None) or (option not in confs)):
        await ctx.send ("你好像打錯什麼了")
      elif ((key == "+") and (option == "admin") and (ans not in confs["admin"])):
        flag = False
        for i in ctx.guild.members:
          if (ans == f"<@{i.id}>"):
            flag = True
            break
          
        if (flag == False):
          await ctx.send ("不對，這個人是誰啊")
          return

        if ((confs["allow_add_by_admin"] == False) and (ctx.author != ctx.guild.owner)):
          await ctx.send ("你好像不能動這個設定欸")
        else:
          confs["admin"].append (ans)
      elif ((key == "-") and (option == "admin") and (ans in confs["admin"])):
        flag = False
        for i in ctx.guild.members:
          if (ans == f"<@{i.id}>"):
            flag = True
            break
          
        if (flag == False):
          await ctx.send ("不對，這個人是誰啊")
          return

        if ((confs["allow_add_by_admin"] == False) and (ctx.author != ctx.guild.owner)):
          await ctx.send ("你好像不能動這個設定欸")
        else:
          confs["admin"].remove (ans)
      elif (key == "set"):
        confs[option] = ans
      else:
        return


      f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "w")
      json.dump (confs, f)
      f.close ()
        
    else:
      await ctx.send ("你是誰啊")
    return

def setup (bot):
  bot.add_cog (configs (bot))
