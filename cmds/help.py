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
      else:
        result = f_res[cate[0]].split ("^")
        if (len (result) <= cate[1] or (cate[1] <= 0)):
          await ctx.send ("沒有這項啦")
        else:
          result = result[cate[1] - 1] 
          await ctx.send (f"```{result}```")
      
    f.close ()
def setup (bot):
  bot.add_cog (help_commands (bot))
