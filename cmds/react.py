import discord
from discord.ext import commands
from core.classes import cog_extension
import random
import json

with open ("config.json", mode = "r", encoding = "utf8") as conf:
  conf_data = json.load (conf)

class react (cog_extension):
  @commands.command ()
  async def gnu頭 (self, ctx):
    random_pic = random.choice (conf_data["pic"])
    pic = discord.File (random_pic)
    await ctx.send (file = pic)
    
def setup (bot):
  bot.add_cog (react (bot))
