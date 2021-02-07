import discord
from time import sleep
import os

client = discord.Client()

@client.event
async def on_message(message):
  if message.content == ';ping' and not message.author.bot:
    await message.channel.send(f'Pong! Heroku latency is {round(client.latency * 1000)}ms')
@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hey! You see my status right? So yeah. PLEASE INPUT YOUR DISCORD USER ID. OR MOD OR STAFF WILL CAN'T REPLY YOU!"))
client.run(os.getenv("TOKEN"))
