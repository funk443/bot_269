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

class role_react (cog_ext):
  @commands.command ()
  async def role_select (self, ctx, contents, *emojis):

    f = open (f"./datas/config/server/svr_conf_{ctx.guild.id}.json", "r")
    conf = json.load (f)
    f.close ()

    if ((f"<@{ctx.author.id}>" not in conf["admin"]) and (ctx.author != ctx.guild.owner)):
      await ctx.message.delete ()
      return

    if (f"role_select_{ctx.guild.id}.json" not in os.listdir ("./datas/role_select")):
      f = open (f"./datas/role_select/role_select_{ctx.guild.id}.json", "w")
      json.dump ({}, f)
      f.close ()

    f = open (f"./datas/role_select/role_select_{ctx.guild.id}.json", "r")
    msgs = json.load (f)
    f.close ()

    await ctx.message.delete ()
    bot_msg = await ctx.send (f">>> {contents}")
    msgs[bot_msg.id] = []

    for i in emojis:
      temp = i.split ("/")
      temp2 = []
      for j in temp:
        temp2.append (j.replace (" ", ""))

      if (len ((temp2[0].split (":"))[-1][:-1]) != 0):
        temp2[0] = int ((temp2[0].split (":"))[-1][:-1])

      temp2[-1] = temp2[-1].split (",")
      msgs[bot_msg.id].append (temp2)

      if (type (temp2[0]) == int):
        await bot_msg.add_reaction (self.bot.get_emoji(temp2[0]))
      else:
        await bot_msg.add_reaction (temp2[0])

    print (msgs)

    f = open (f"./datas/role_select/role_select_{ctx.guild.id}.json", "w")
    json.dump (msgs, f)
    f.close ()

  @commands.Cog.listener ()
  async def on_raw_reaction_add (self, payload):
    if (f"role_select_{payload.guild_id}.json" not in os.listdir ("./datas/role_select")):
      return

    if (payload.member.bot == True):
      return

    f = open (f"./datas/role_select/role_select_{payload.guild_id}.json", "r")
    msgs = json.load (f)
    f.close ()

    if (str (payload.message_id) not in msgs):
      return

    # usr = payload.member
    # print (type (usr))

    for i in msgs[str (payload.message_id)]:
      if (payload.emoji.is_unicode_emoji ()):
        if (i[0] == str (payload.emoji)):
          for j in i[-1]:
            server = self.bot.get_guild (payload.guild_id)
            role = server.get_role (int (j[3:-1]))

            await payload.member.add_roles (role)
      else:
        if (i[0] == payload.emoji.id):
          for j in i[-1]:
            server = self.bot.get_guild (payload.guild_id)
            role = server.get_role (int (j[3:-1]))

            await payload.member.add_roles (role)
          
def setup (bot):
  bot.add_cog (role_react (bot))
