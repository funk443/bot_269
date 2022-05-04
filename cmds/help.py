import discord
import json
import os
from core.classes import cog_ext
from discord.ext import commands
from orgparse import load, loads

class help_commands (cog_ext):
  @commands.command ()
  async def help (self, ctx, cate = None):
    # await ctx.send ("還在寫，不要急。先給你可以用的指令列表:")
    # help_file = load ("./resources/help.org")

    # if (cate == None):
    #   for i in help_file:
    #     await ctx.send (i)
    f = open ("./resources/help.txt", "r")
    f_res = f.read ().split ("&")
      

    if (cate == None):
      await ctx.send (f"```{f_res[0]}```")
    else:
      cate = list (map (int, cate.split(".")))

      if (len (cate) == 1):
        await ctx.send (f"```{f_res[cate[0] - 1]}```")
      else:
        result = f_res[cate[0] - 1].split ("^")
        result = result[cate[1] - 1] 
        await ctx.send (f"```{result}```")
      
    f.close ()
def setup (bot):
  bot.add_cog (help_commands (bot))
