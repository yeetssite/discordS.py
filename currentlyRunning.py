#!/data/data/com.termux/files/usr/bin/python
# Import stuff

import discord # external
from discord.ext import commands, tasks # external
from dotenv import load_dotenv # external
import os 
import time
import random
from prompt_toolkit import PromptSession # external
from sys import argv
from sys import exit as quitbot
from sys import stdout
from os import system
import asyncio
from functools import partial
# Simplify some stuff

system("clear")

intents = discord.Intents.all()

session = PromptSession(message="message: ")

# Load .env file(add environmental variables, used for security purposes)

load_dotenv()

# check arguments
try:
    if argv[1] == "sendmsg":
        try:
            startmessage = argv[2]
        except Exception as err:
            print("[31;1mNo message to send:[m "+str(err)+".")
    else:
        startmessage = False
    if "--no-greet" in argv:
        greeting = False
    else:
        greeting = True
    if argv[1] == "dmuser":
        try:
            dmUser=True
            dmUserID = argv[2]
            try:
                dmUserMsg = argv[3]
            except Exception as err:
                dmUser = False
                print("[1;31mNo message to send:[m "+str(err)+".")
        except Exception as err:
            dmUser = False
            print("[1;31mNo user to send a dm to:[m "+str(err)+".")
    else:
        dmUser = False
except IndexError:
    startmessage = False
    greeting = True
    dmUser = False


# Version stuff

version = 1.2
devstage = str("alpha")

# Copyright, license, and credit

author = str("Jacob \"yeetsup\" Haché")
copyright = str("Copyright (c) 2024-2026 Jacob \"yeetsup\" Haché, from canada")
license = str("This bot is licensed under the GNU Public License 3.0(GPL-3.0).\n"+"See http://fsf.org/licenses/gpl-3.0 .")

# Discord bot variables

botToken = str(os.environ["botToken"])
bot = commands.Bot(intents=intents , command_prefix="tf:")

join_msgs = ["I have awaken", "A RED spy has entered the base", "Don't worry pookies, daddy's here", "Whats up you dumb niggers", "haiii :3", "E", "I have been re(s)tarded."]

memes = ["https://yeetssite.github.io/memes/IMG/17.jpg", "https://yeetssite.github.io/memes/IMG/GIF_001.gif", "https://yeetssite.github.io/memes/IMG/IMG_001.png", "https://yeetssite.github.io/memes/IMG/IMG_002.png", "https://yeetssite.github.io/memes/IMG/IMG_003.png", "https://yeetssite.github.io/memes/IMG/IMG_004.jpg", "https://yeetssite.github.io/memes/IMG/IMG_005.jpg", "https://yeetssite.github.io/memes/IMG/IMG_006.jpg", "https://yeetssite.github.io/memes/IMG/IMG_007.png", "https://yeetssite.github.io/memes/IMG/IMG_008.png", "https://yeetssite.github.io/memes/IMG/IMG_009.png", "https://yeetssite.github.io/memes/IMG/IMG_010.png", "https://yeetssite.github.io/memes/IMG/IMG_011.png", "https://yeetssite.github.io/memes/IMG/IMG_012.JPEG", "https://yeetssite.github.io/memes/IMG/IMG_013.png", "https://yeetssite.github.io/memes/IMG/IMG_014.png", "https://yeetssite.github.io/memes/IMG/IMG_015.png", "https://yeetssite.github.io/memes/IMG/IMG_016.png", "https://yeetssite.github.io/memes/IMG/IMG_017.png", "https://yeetssite.github.io/memes/IMG/IMG_018.JPEG", "https://yeetssite.github.io/memes/IMG/IMG_019.png", "https://yeetssite.github.io/memes/IMG/IMG_020.png", "https://yeetssite.github.io/VIDEO/VIDEO_001.mp4", "https://yeetssite.github.io/TROLL.MP4", "https://media.discordapp.net/attachments/1360347348831568099/1360669610256371773/T-1000_Chases_Forrest_Gump_nRH_IiloXPU.webm?ex=6973b153&is=69725fd3&hm=fb11e28a468e1c08ec3710f79641c08af3df6f4599731c10287dc137919b75b6&"]

andypics = ["https://cdn.discordapp.com/attachments/1360347348831568099/1360350188316655806/IMG_6233.jpg?ex=6973d956&is=697287d6&hm=1f3284c00f2fd1b8412161ce1751ec6c1fce0acbc95aa56de17310d757b12204&", "https://cdn.discordapp.com/attachments/1360347348831568099/1360353800082423949/retouch_2025040319163847.jpg?ex=6973dcb4&is=69728b34&hm=ba8fdb97e9477c179517bc6e7e388143a52012e431bfdd559b62c7ff631d61ec&", "https://cdn.discordapp.com/attachments/1360347348831568099/1456396256279658577/654dacc4-f3a2-4264-9358-7af97aed5761.gif?ex=6973e5b6&is=69729436&hm=6330e1c6ddfa76f3fbb6b4e594aab9c29048c440365dc57618b7fc4968f07f6e&", "https://cdn.discordapp.com/attachments/1360347348831568099/1461799247925219458/IMG_1380.jpg?ex=6973c723&is=697275a3&hm=766d5d0b5ea604aa150e863678eaeb5e557bf9193a2a27f7e1f8364d15f4601d&", "https://cdn.discordapp.com/attachments/1360347348831568099/1461393882523766825/IMG_4042.jpg?ex=69739f1c&is=69724d9c&hm=4ba15d1098b3f8128dd192e7566ec45d2f9974d4310ff87671ccbc28d602f1f8&", "https://cdn.discordapp.com/attachments/1360347348831568099/1461393719226798144/IMG_20260115_091609.jpg?ex=69739ef6&is=69724d76&hm=d3291ca12994e87af9b05b5a2acacb07e8138b071457fb5a474dde8646368826&", "https://cdn.discordapp.com/attachments/1360347348831568099/1459621250765950987/mustard.jpg?ex=6973c3b8&is=69727238&hm=c479ed483578fb9404010ae78ee75d5b6749cdf317250d92d694246c0b6f54d6&", "https://cdn.discordapp.com/emojis/1275359175563808781.png?quality=lossless&name=thereisnoeasterbunny&size=48", "https://cdn.discordapp.com/attachments/1360347348831568099/1389068285235953784/retouch_2025062920211814.jpg?ex=697383e6&is=69723266&hm=5d15398e8da2772c48737bcb0c979b62bed71b17cab5f5a33909a793dd900c3e&", "https://cdn.discordapp.com/attachments/1293750492932870184/1356071411126370314/5428fe1e3a5de9f99e2b3a91277da122-3118236496.jpg?ex=697371ab&is=6972202b&hm=ca661a0003285a36801939c5663146d0840213c8ab540c01dfdbf4573576d710&", "https://media.discordapp.net/attachments/1126973631579308076/1324784495680946236/Screenshot_20250103-100015.jpg?ex=6973a935&is=697257b5&hm=98cdf420e1c22ce216f95fc3b5b804d1e22eca574631b5c327a650459d8b0d62&", "https://media.discordapp.net/attachments/1126973631579308076/1324784495680946236/Screenshot_20250103-100015.jpg?ex=6973a935&is=697257b5&hm=98cdf420e1c22ce216f95fc3b5b804d1e22eca574631b5c327a650459d8b0d62&"]

# Bot events/commands

def printMsg(content): # This function should only be used in a @bot.event,
                # as it requires all the ctx variables created by the event.
   print("[4;34m" + serverName + "[0m | [1;35m" + channelName + "[m")
   print("[44;30m" + userName + "[0;1;30m(" + userID + ") [m | [3m" + timestamp + "[m")
   print(content)

@bot.event
async def on_ready():
   botID = str(bot.user.id)
   botUsername = str("@" + bot.user.name)
   print("[1;35mThe discord [31ms.py [34mv" + str(version) + "[32m " + devstage + "[37m by [31m" + author)
   print("[30m"+copyright)
   print(license+"[m")
   print("[31mA RED SPY IS IN THE BASE.[0m And he's logged onto Discord with the user ID:\n"\
         + botID + "\n"\
         "And the username:\n"\
         + botUsername + "\n"\
        )
   sfc = bot.get_channel(1163807068290031670)
   if not startmessage:
    if greeting:
        await sfc.send(random.choice(join_msgs) + " (yeet's bot online)")
   else:
    await sfc.send(startmessage)
   if dmUser:
       toDM = await bot.fetch_user(int(dmUserID))
       DMchan = await toDM.create_dm()
       print("Opened a DM with "+DMchan.recipient.name)
       await DMchan.send(dmUserMsg)
# set up reply prompt

async def get_input_from_user():
    command = await bot.loop.run_in_executor(None, session.prompt)
    return command

@tasks.loop(seconds=5.0, count=1)
async def replyPrompt(msg, noreply=False):
    replyMsg = await get_input_from_user()
    if replyMsg.startswith("/"):
        if replyMsg == "/meme":
            replyMsg = random.choice(memes)
        elif replyMsg == "/kill" or replyMsg == "/exit":
            system("clear")
            literallyNothing = open(os.devnull, "w")
            stdout = literallyNothing
            quitbot(0)
    if not noreply:
        await msg.reply(replyMsg)
    else:
        await msg.channel.send(replyMsg)

async def promptExit():
    await command.cancel()

async def killPrompt():
    await promptExit()
@bot.command()
async def meme(ctx):
    await ctx.reply(random.choice(memes))

@bot.command()
async def jew(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/1360347348831568099/1463326336851640537/17689543594313781603057425671703.gif?ex=69740f59&is=6972bdd9&hm=6de43081123c81bf9e36cad6daf11ab0d2c9c8e787f6e2877dd12aaee0937452&")

@bot.command()
async def andrew(ctx):
    pic = random.choice(andypics)
    if not pic == "https://media.discordapp.net/attachments/1126973631579308076/1324784495680946236/Screenshot_20250103-100015.jpg?ex=6973a935&is=697257b5&hm=98cdf420e1c22ce216f95fc3b5b804d1e22eca574631b5c327a650459d8b0d62&":
        pic = random.choice(andypics)
    await ctx.reply(pic)
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
   dmAuthors = []
   dmMsgCnt = 0
   userID = str(ctx.author.id)
   userName = str("@" + ctx.author.name)
   botID = str(bot.user.id)
   botUsername = str(bot.user.name)
   msgContent = str(ctx.content)
   try:
     serverName = str(ctx.guild.name)
     channelName = str("#" + ctx.channel.name)
     dms = False
   except AttributeError:
     serverName = str("DIRECT MESSAGES")
     try:
         channelName = channelName
     except:
         dmName = str("@"+ctx.author.name)
         channelName = dmName
     if not userID == botID:
        dmrecipient = await bot.fetch_user(userID)
        opendm = await dmrecipient.create_dm()
        channelName = opendm.recipient.name
     dms = True
   timestamp = str(time.strftime('%H:%M:%S'))
   # check for attachments
   if len(ctx.attachments) > 0:
     print("\n\a[1;32m——————Start of attachments——————[m")
     for file in ctx.attachments:
         if file == ctx.attachments[0]:
             if not msgContent:
                 printMsg(str(file.url))
             else:
                 printMsg(msgContent +"\n[1;30m————————————————————[0m\n" + str(file.url))
         else:
             print("[1;30m————————————————————[0m")
             print(str(file.url))
     print("[1;32m———————End of attachments———————[m")
   # do shit if no attachments
   else:
     print("\n\a[1;33m——————Start of message——————[m")
     printMsg(msgContent)
     print("[1;33m———————End of message———————[m")
   # allow replying to mentions and messages
   if bot.user.mentioned_in(ctx):
     prev_author = userID
     if replyPrompt.is_running():
         pass
     else:
         replyPrompt.start(ctx)
   if dms:
     if replyPrompt.is_running():
         pass
     else:
         replyPrompt.start(ctx, noreply=True)

   if "jew" in ctx.content.lower() or "desk" in ctx.content.lower():
       await ctx.reply("https://cdn.discordapp.com/attachments/1360347348831568099/1463326336851640537/17689543594313781603057425671703.gif?ex=69740f59&is=6972bdd9&hm=6de43081123c81bf9e36cad6daf11ab0d2c9c8e787f6e2877dd12aaee0937452&", mention_author=False)
   await bot.process_commands(ctx)
   
@bot.event
async def on_message_edit(og,ctx):
   global userID
   global userName
   global botID
   global botUsername
   global serverName
   global msgContent
   global ogMsgContent
   global channelName
   global timestamp
   userID = str(ctx.author.id)
   userName = str("@" + ctx.author.name)
   botID = str(bot.user.id)
   botUsername = str(bot.user.name)
   msgContent = str(ctx.content)
   ogMsgContent = str(og.content)
   serverName = str(ctx.guild.name)
   channelName = str("#" + ctx.channel.name)
   timestamp = str(time.strftime('%H:%M:%S'))

   print("\n\a[1;34m——————Edited message——————[0m")
   print("[1;30m———Original message———")
   print(ogMsgContent + "[0m")
   printMsg(msgContent)
   print("[1;34m————End edited message————[0m")

@bot.event
async def on_message_delete(ctx):
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

   print("\n\a[1;31m——————Deleted message——————[0m")
   printMsg(msgContent)
   print("[1;31m————End deleted message————[0m")

bot.run(botToken)


