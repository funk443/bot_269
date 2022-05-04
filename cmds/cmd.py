import discord
import json
import random
from discord.ext import commands
from core.classes import cog_ext

js = open ("config.json")
conf = json.load (js)
js.close ()

class cmd (cog_ext):
  @commands.command ()
  async def reply (self, ctx, key, content_1 = None, content_2 = None):
    f = open ("data.json", "r")
    data = json.load (f)
    f.close ()

    if (key == "add"):
      if (content_2 == None):
        await ctx.send ("你是要我加什麼啦")
      else:
        f = open ("data.json", "w")
        data[str (content_1)] = str (content_2)
        json.dump (data, f)
        f.close ()

        await ctx.send (f"added {content_1}")

    elif (key == "del"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我是要刪什麼啦")
      else:
        if (content_1 in data):
          f = open ("data.json", "w")
          data.pop (content_1)
          json.dump (data, f)
          f.close ()
          await ctx.send ("del")
        else:
          await ctx.send ("先生，沒有那種東西")

    elif (key == "find"):
      if (content_1 == None):
        await ctx.send ("你沒給我東西我是要怎麼找啦")
      else:
        if (content_1 in data):
          await ctx.send (data[content_1])
        else:
          await ctx.send ("先生，沒有那種東西")
                             
    elif (key == "list"):
      if (len (data) != 0):
        for i in data:
          await ctx.send (f"```{i}:{data[i]}```")
      else:
        await ctx.send ("竟然一個東西都沒有")
          
    else:
      on_command_error (self, ctx, none)

def setup (bot):
  bot.add_cog (cmd (bot))
