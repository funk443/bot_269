import discord
import json
import os
from core.classes import cog_ext
from discord.ext import commands


class help_commands (cog_ext):
  @commands.command ()
  async def help (self, ctx, cate = None):
    await ctx.send ("還在寫，不要急。先給你可以用的指令列表:")
    for i in (self.bot.commands):
      await ctx.send (f"```{i}```")
    
def setup (bot):
  bot.add_cog (help_commands (bot))
