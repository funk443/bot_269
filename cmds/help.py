import discord
import json
import os
from core.classes import cog_ext
from discord.ext import commands
from orgparse import load, loads

class help_commands (cog_ext):
  @commands.command ()
  async def help (self, ctx, cate = None):
    await ctx.send ("還在寫，不要急。先給你可以用的指令列表:")
    help_file = load ("./resources/help.org")

    if (cate == None):
      for i in help_file:
        await ctx.send (i)
    
def setup (bot):
  bot.add_cog (help_commands (bot))
