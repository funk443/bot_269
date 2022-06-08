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
import datetime
import random
from discord.ext import commands
from core.classes import cog_ext

options = ("大吉", "吉", "小吉", "平", "小凶", "凶", "大凶", "你命由你不由天，自己幸福自己拼")

class luck (cog_ext):
  @commands.command ()
  async def 今日運勢 (self, ctx):
    f = open ("./datas/luck.json", "r", encoding = "utf-8")
    last_time = json.load (f)
    f.close ()

    f = open ("./datas/luck.json", "w", encoding = "utf-8")
    if (str (ctx.author.id) not in last_time):
      today_luck = random.choice (options)
      await ctx.reply (today_luck)
      last_time[str (ctx.author.id)] = [str (ctx.message.created_at.date ()), today_luck]

      json.dump (last_time, f)
      f.close ()
      return

    delta = ctx.message.created_at.date () - datetime.date.fromisoformat (last_time[str (ctx.author.id)][0])

    if (delta.days == 0):
      today_luck = last_time[str (ctx.author.id)][1]
      await ctx.reply (f"你是要問幾次啦，就跟你說今天是 {today_luck} 了")
    else:
      today_luck = random.choice (options)
      await ctx.reply (today_luck)
      last_time[str (ctx.author.id)] = [str (ctx.message.created_at.date ()), today_luck]

    # print (datetime.date.today () - datetime.date.fromisoformat (last_time[ctx.author.id]))
    json.dump (last_time, f)
    f.close ()


def setup (bot):
  bot.add_cog (luck (bot))
