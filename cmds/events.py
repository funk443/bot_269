import discord
import json
import random
from discord.ext import commands
from core.classes import cog_ext

js = open ("config.json")
conf = json.load (js)
js.close ()

class events (cog_ext):
  @commands.Cog.listener ()
  async def on_member_join (self, member):
    channel = self.bot.get_channel (conf["general"])
    await channel.send (f"Welcome, {member.mention}")

  @commands.Cog.listener ()
  async def on_member_leave (self, member):
    channel = self.bot.get_channel (conf["general"])
    await channel.send (f"Goodbye, {member.mention}")
  
  @commands.Cog.listener ()
  async def on_message (self, message):
    if (message.author == self.bot.user):
      return

    if ("linux" in message.content.lower ().split ()):
      f = open (conf["GNULinux"], "r")
      await message.channel.send (f.read ())
      f.close ()
  
  @commands.Cog.listener ()
  async def on_message_edit (self, before, after):
    if (before.author == self.bot.user):
      return
  
    word = random.choice (conf["kai"])
    await before.reply (word)

  @commands.Cog.listener ()
  async def on_command_error (self, ctx, error):
    word = random.choice (conf["wtf"])
    await ctx.reply (word)

def setup (bot):
  bot.add_cog (events (bot))
