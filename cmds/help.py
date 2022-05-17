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
from core.classes import cog_ext
from discord.ext import commands

class help_commands (cog_ext):
  @commands.command ()
  async def help (self, ctx, cate = None):
    f = open ("./resources/help.txt", "r")
    f_res = f.read ().split ("&")
      

    if (cate == None):
      await ctx.send (f"```{f_res[0]}```")
    else:
      cate = list (map (int, cate.split(".")))

      if (len (cate) == 1):
        await ctx.send (f"```{f_res[cate[0]]}```")
      # else:
      #   result = f_res[cate[0]].split ("^")
      #   if (len (result) <= cate[1] or (cate[1] <= 0)):
      #     await ctx.send ("沒有這項啦")
      #   else:
      #     result = result[cate[1] - 1] 
      #     await ctx.send (f"```{result}```")
      
    f.close ()
def setup (bot):
  bot.add_cog (help_commands (bot))
