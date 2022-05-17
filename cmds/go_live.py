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
from discord.ext import commands, tasks
from twitchAPI.twitch import Twitch

f = open ("twitch.json", "r")
tch = json.load (f)
f.close ()
twitch = Twitch(tch["key"], tch["secret"])

twitch_names = []
twitch_chan = []
twitch_stat = []
twitch_content = []
twitch_ebd = []
files_list = os.listdir ("datas/config/server")
files_list.remove ("a")
files_list.remove ("default.json")
for i in files_list:
  f = open (f"datas/config/server/{i}", "r")
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


class go_live (commands.Cog):
  def __init__ (self, bot):
    self.bot = bot
    self.check_live.start (twitch_names, twitch_chan, twitch_stat,
                           twitch_content, twitch_ebd)

  @tasks.loop (minutes = 1)
  async def check_live (self, users, chan, stat, content, ebd):
    # print (users, chan, stat, content, ebd)
    last_stat = stat.copy ()
    for i in range (len (stat)):
      last_stat[i] = stat[i].copy ()

    for i in range (len (users)):
      data = twitch.get_streams (user_login = users[i])["data"]
      # print (data)
      on_usrs = []
      # print (type (ebd))
  
      for j in data:
        if (j["user_login"] in users[i]):
          stat[i][users[i].index (j["user_login"])] = True
          on_usrs.append (j["user_login"])
  
      off_usrs = list (set (users[i]) - set (on_usrs))
  
      for j in off_usrs:
        stat[i][users[i].index (j)] = False
  
      go_live_usr = []
  
      for j in range (len (stat[i])):
        if ((stat[i][j] == True) and (last_stat[i][j] == False)):
          go_live_usr.append (users[i][j])
          usr = users[i][j]
          data_index = on_usrs.index (users[i][j])
          chan_id = await self.bot.fetch_channel (int (chan[i]))
          usr_info = twitch.get_users (logins = [users[i][j]])["data"][0]
          # print (usr_info)
          if (ebd[i]):
            embed = discord.Embed (title = data[data_index]["title"], description = f"{data[data_index]['user_name']} 在圖奇開台了!",
                                   url = f"https://www.twitch.tv/{usr}")
            embed.set_author (name = f"{data[data_index]['user_name']}({usr})", url = f"https://www.twitch.tv/{usr}",
                              icon_url = usr_info["profile_image_url"])
            embed.add_field (name = "正在玩", value = data[data_index]["game_name"])
            embed.set_image (url = data[data_index]["thumbnail_url"].replace ("{width}", "1920").replace ("{height}", "1080"))
            embed.set_footer (text = "Twitch", icon_url = "https://cdn.discordapp.com/attachments/967880010281123913/975095292087124048/twitch.png")
            await chan_id.send (content = f"{content[i]} https://www.twitch.tv/{usr}", embed = embed)
          else:
            await chan_id.send (content = f"{content[i]} https://www.twitch.tv/{usr}")

def setup (bot):
  bot.add_cog (go_live (bot))
