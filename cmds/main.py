import discord
from discord.ext import commands
from core.classes import cog_extension
import datetime as dt
from dateutil import tz

class main (cog_extension):

  @commands.command ()
  async def ping (self, ctx):
    await ctx.send (f"{round (self.bot.latency * 1000)} ms")

  @commands.command ()
  async def fsf (self, ctx):
    embed=discord.Embed (title = "100% Free!!", url = "https://www.gnu.org",
                         description = "As in Freedom.",
                         timestamp = dt.datetime.now (tz.tzlocal ())) 
    embed.set_author (name = "RMS", url = "https://stallman.org/")
    embed.set_thumbnail (url = "https://www.gnu.org/graphics/heckert_gnu.png")
    embed.set_footer (text = "support fsf")
    await ctx.send (embed=embed)


def setup (bot):
  bot.add_cog (main (bot))
