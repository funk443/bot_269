import discord
from discord.ext import commands
from core.classes import cog_extension
import random
import json

with open ("config.json", mode = "r", encoding = "utf8") as conf:
  conf_data = json.load (conf)

class events (cog_extension):
  @commands.Cog.listener ()
  async def on_member_join (self, member):
    print (f"{member} joined!")
    channel = self.bot.get_channel (int(conf_data["general"]))
    await channel.send (f"{member} joined!")
    
  @commands.Cog.listener ()
  async def on_member_remove (self, member):
    print (f"{member} left!")
    channel = self.bot.get_channel (int(conf_data["general"]))
    await channel.send (f"{member} left!")

  @commands.Cog.listener ()
  async def on_message (self, msg):
    if (((msg.content.lower ()).find ("linux") != -1)
        & ((msg.content.lower ()).find ("gnu/linux") == -1)
        & (msg.author != self.bot.user)):
      f = open (conf_data["txt"])
      await msg.channel.send (f.read ())
      
      
def setup (bot):
  bot.add_cog (events (bot))
