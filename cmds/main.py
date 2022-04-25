import discord
from discord.ext import commands
from core.classes import cog_extension

class main (cog_extension):

  @commands.command ()
  async def ping (self, ctx):
    await ctx.send (f"{round (self.bot.latency * 1000)} ms")

def setup (bot):
  bot.add_cog (main (bot))
