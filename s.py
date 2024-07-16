#!/data/data/com.termux/files/usr/bin/python
# Import stuff

import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
import os
import time

# Simplify some discord stuff

intents = discord.Intents.all()


# Load .env file(add environmental variables, used for security purposes)

load_dotenv()

# Version stuff

version = str("1.0.0")
devstage = str("alpha")

# Copyright, license, and credit

author = str("Jacob \"yeetsup\" Haché")
copyright = str("Copyright (c) 2024 Jacob \"yeetsup\" Haché, from canada")
license = str("This bot is licensed under the GNU Public License 3.0\(GPL-3.0\).\n"+\
              "See http://fsf.org/licenses/gpl-3.0 .")

# Discord bot variables

botToken = str(os.environ["botToken"])
bot = commands.Bot(intents=intents , command_prefix="tf:")

# Bot events/commands

@bot.event
async def on_ready():
   botID = str(bot.user.id)
   botUsername = str("@" + bot.user.name)
   print("[31mA RED SPY IS IN THE BASE.[0m And he's logged onto Discord with the user ID:\n"\
         + botID + "\n"\
         "And the username:\n"\
         + botUsername + "\n"\
        )


def printMsg(): # This function should only be used in a @bot.event, 
                # as it requires all the ctx variables created by the event.
   print("[4;34m" + serverName + "[0m | [1;35m" + channelName + "[0m")
   print("[44;30m" + userName + "[0;1;30m(" + userID + ") [0m | [3m" + timestamp + "[0m")
   print(msgContent)

@bot.event
async def on_message(ctx):
   global userID
   global userName
   global botID
   global botUsername
   global serverName
   global msgContent
   global channelName
   global timestamp
   userID = str(ctx.author.id)
   userName = str("@" + ctx.author.name)
   botID = str(bot.user.id)
   botUsername = str(bot.user.name)
   msgContent = str(ctx.content)
   serverName = str(ctx.guild.name)
   channelName = str("#" + ctx.channel.name)
   timestamp = str(time.strftime('%H:%M:%S'))

   print("\n\a[1;33m——————Start of message——————[m")
   printMsg()
   print("[1;33m——————End of message——————[m")
   await bot.process_commands(ctx)



bot.run(botToken)



