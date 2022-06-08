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
from cmds.go_live import go_live


class configs (go_live):
  @commands.command ()
  async def usr_conf (self, ctx):
    if (f"usr_conf_{ctx.author.id}.json" not in os.listdir("./datas/config/user")):
      f = open (f"./datas/config/user/usr_conf_{ctx.author.id}.json", "w", encoding = "utf-8")
      json.dump ({}, f)
      f.close ()
    return

  @commands.command ()
  async def svr_conf (self, ctx, key = None, option = None, ans = None):
    f = open (f"./datas/config/server/default.json", "r", encoding = "utf-8")
    default = json.load (f)
    f.close ()

    if (f"svr_conf_{ctx.guild.id}.json" not in os.listdir("./datas/config/server")):
      f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "w", encoding = "utf-8")
      json.dump (json.load (default), f)
      f.close ()

    f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "r", encoding = "utf-8")
    confs = json.load (f)
    f.close ()

    diff = {k:default[k] for k  in set (default) - set (confs)}
    confs = diff | confs

    if ((f"<@{ctx.author.id}>" in confs["admin"]) or (ctx.author == ctx.guild.owner)):
      if (key == None):
        await ctx.send (f"`{confs}`")
      elif ((key == "clr") and (option == "twitch_name")):
        confs[option] = []
      elif ((option == None) or (ans == None)):
        await ctx.send ("你好像打錯什麼了")
      elif ((key == "+") and (option == "admin") and (ans not in confs["admin"])):
        flag = False
        for i in ctx.guild.members:
          if (ans == f"<@{i.id}>"):
            flag = True
            break
          
        if (flag == False):
          await ctx.send ("不對，這個人是誰啊，這個伺服器沒有這個人啊")
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
          await ctx.send ("不對，這個人是誰啊，這個伺服器沒有這個人啊")
          return

        if ((confs["allow_add_by_admin"] == False) and (ctx.author != ctx.guild.owner)):
          await ctx.send ("你好像不能動這個設定欸")
        else:
          confs["admin"].remove (ans)
      elif (key == "set"):
        if (option == "admin"):
          await ctx.send ("這個不是用set啦")
          return

        if (((option == "twitch_embed") or (option == "allow_add_by_admin")) and (ans not in ["true", "false"])):
          await ctx.send ("你大概打錯什麼東西了")
        elif (option == "twitch_name"):
          ans = ans.split (",")

          confs[option] = ans
        elif (option == "twitch_noti_chan"):
          confs[option] = ans[2:-1]
        else:
          confs[option] = ans
      else:
        return

      f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "w", encoding = "utf-8")
      json.dump (confs, f)
      f.close ()

      twitch_names = []
      twitch_chan = []
      twitch_stat = []
      twitch_content = []
      twitch_ebd = []
      files_list = os.listdir ("datas/config/server")
      files_list.remove ("a")
      files_list.remove ("default.json")
      for i in files_list:
        f = open (f"datas/config/server/{i}", "r", encoding = "utf-8")
        svr_conf = json.load (f)
        f.close ()
        stat = []
      
        twitch_names.append (svr_conf["twitch_name"])
        twitch_chan.append (svr_conf["twitch_noti_chan"])
        for j in svr_conf["twitch_name"]:
          stat.append (False)
      
        twitch_stat.append (stat)
        twitch_content.append (svr_conf["twitch_noti_text"])
        twitch_ebd.append (svr_conf["twitch_embed"])
        
      if ((key != None) and ((option == "twitch_name") or (option == "twitch_noti_chan"))):
        go_live.check_live.cancel ()
        go_live.check_live.start (self, users = twitch_names, chan = twitch_chan, stat = twitch_stat,
                                  content = twitch_content, ebd = twitch_ebd)

    else:
      await ctx.send ("你是誰啊")

def setup (bot):
  bot.add_cog (configs (bot))
