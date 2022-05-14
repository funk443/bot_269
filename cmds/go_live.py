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
from core.classes import cog_ext

f = open ("twitch.json", "r")
tch = json.load (f)
f.close ()
twitch = Twitch(tch["key"], tch["secret"])

class go_live (cog_ext):
  @tasks.loop (minutes = 1)
  async def check_live (self, users, chan, stat, content):
    last_stat = stat.copy ()
    data = twitch.get_streams (user_login = users)["data"]
    on_usrs = []
    # print (users)

    for i in data:
      if (i["user_login"] in users):
        stat[users.index (i["user_login"])] = True
        on_usrs.append (i["user_login"])

    off_usrs = list (set (users) - set (on_usrs))

    for i in off_usrs:
      stat[users.index (i)] = False

    go_live_usr = []

    for i in range (len (stat)):
      if ((stat[i] == True) and (last_stat[i] == False)):
        go_live_usr.append (users[i])
        usr = users[i]
        chan = self.bot.get_channel (int (chan))
        await chan.send (f"{content} https://www.twitch.tv/{usr}")

    # print (on_usrs)
    # print (off_usrs)
    # print (go_live_usr)
    # print (stat)
    # print (last_stat)

def setup (bot):
  bot.add_cog (go_live (bot))
