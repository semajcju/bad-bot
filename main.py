import discord
import os
import time
import random
import multiprocessing

from discord import message

cancel = False

client = discord.Client()

@client.event
async def cancel():
  if message.author == client.user:
    return
  
  if message.startswith('!cancel'):
    cancel = True


@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

#@client.event
#def printfile(script):
#  file = open(script)
#  lines = file.readlines()
#  linenum = 0
#  for line in lines:
#    await message.channel.send(line)
#    linenum + 1
#    time.sleep(1)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('@everyone') or msg.startswith('cant'):
    option = random.randint(1, 3)
    if option == 1:
      file = open("bee movie.txt")
      lines = file.readlines()
      linenum = 0
      for line in lines:
        if cancel == True:
          cancel == False
          break
        await message.channel.send(line)
        linenum + 1
        time.sleep(1)
    elif option == 2:
      file = open("never gonna give you up.txt")
      lines = file.readlines()
      linenum = 0
      for line in lines:
        if cancel == True:
          cancel == False
          break
        await message.channel.send(line)
        linenum + 1
        time.sleep(1)
    elif option == 3:
      file = open("shrek.txt")
      lines = file.readlines()
      linenum = 0
      for line in lines:
        if cancel == True:
          cancel == False
          break
        await message.channel.send(line)
        linenum + 1
        time.sleep(1)



client.run(os.getenv('TOKEN'))

