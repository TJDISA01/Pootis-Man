# https://discordpy.readthedocs.io/en/latest/api.html
import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import opus_api
import youtube_dl
import time

token = os.environ.get("DISCORD_BOT_SECRET")
bot = commands.Bot(command_prefix="::", description="The Pootis Man.")
discord.opus.load_opus()
# bot.remove_command(help)

@bot.event
async def on_ready():
  print("I'm running!")
  print(bot.user)
  await bot.change_presence(game=discord.Game(name='::commands'))

@bot.event
async def on_member_join(member):
  prefix = bot.user.nick.split(" ")[0]
  nick = member.nick.split(" ")
  nick.insert(0, prefix)
  new_nick = " ".join(member.nick)
  await bot.change_nickname(member, new_nick)
  await bot.say(f"{member} has joined the server! Their new nickname is {new-nick}")

@bot.command()
async def commands():
  await bot.say("!p https://www.youtu.be/EM4iQn2Si-U")
  await bot.say("::commands -- The following list of commands.")
  await bot.say("::exit -- Makes the bot logout, in case of bugging.")
  await bot.say("::merasmus -- Say hello to your worst roommate!")
  await bot.say("::hoovy -- Put dispenser here!")
  await bot.say("::nickname (prefix) -- Changes the nickname of each server member to the desired prefix.")
  await bot.say("::voice (class) (line) -- Work in progress!")
  await bot.say("::thomasonreddit -- When Thomas starts talking about Reddit memes about something only he understands.")

@bot.command()
async def merasmus():
  await bot.say("Merasmus the Wizard has come for you souls!")
  time.sleep(1)
  await bot.say("Oh, hello Soldier.")
  time.sleep(1)
  await bot.say("What are you holding?")
  time.sleep(1)
  await bot.say("*Soldier hands him the rent*")
  time.sleep(1)
  await bot.say("This is a bomb, isn't it?")
  time.sleep(1)
  await bot.say("*Hand back Bombinomicon*")
  time.sleep(1)
  await bot.say("*Explodes*")
  time.sleep(1)
  await bot.say("Damn you Soldier! *You were the worst roommaaaaaaaaaaate!*")

@bot.command()
async def hoovy():
  await bot.say("Pootis!")
  time.sleep(1)
  await bot.say("*Throws Sandvich*")
  time.sleep(1)
  await bot.say("*He readies his taunt as you turn away*")
  time.sleep(1)
  await bot.say("POW! Haha!")
  time.sleep(1)
  await bot.say("You are dead, not big suprise.")

@bot.command(pass_context=True)
async def nickname(ctx, prefix):
  # if ctx.message.server.channel.id != "514443208395063296":
  #   await bot.say("Please use the Bot Channel, as this command returns many messages!")
  # else:
    print(ctx.message.server.members)
    for member in ctx.message.server.members:
      # Mark & his bot have highest status, cannot be changed
      if member.id == "298657894428049411" or member.id == "491434154093838336":
        continue
      print(member)
      new_nick = member.nick.split(" ")
      del new_nick[0]
      new_nick.insert(0, prefix)
      print(new_nick)
      new_nick = " ".join(new_nick)
      print(new_nick)
      await bot.change_nickname(member, new_nick)
      await bot.say(f"{member}'s nickname was changed!")
    await bot.say(f"Everyone has been given the prefix {prefix}!")
    # await bot.say("Use '/nick' to change your own Nickname on a server!\n(Leave some kind of word before your name to save me some trouble later!)")

@bot.command(pass_context=True)
async def thomasonreddit(ctx):
  # RuntimeError: PyNaCl library needed in order to use voice.
  # Even snakes need salt to work properly.
  channel = ctx.message.author.voice.voice_channel
  await bot.join_voice_channel(channel)
  voice_client = bot.voice_client_in(channel)
  voice_client.create_stream_player("https://www.youtu.be/2aegP8j5al0")
  await voice_client.disconnect()
  await bot.say("!p https://www.youtu.be/2aegP8j5al0")

@bot.command()
async def exit():
  await bot.say("Closing bot...")
  await bot.logout()

@bot.command(pass_context=True)
async def dc(ctx):
  channel = ctx.message.author.voice.voice_channel
  voice_client = bot.voice_client_in(channel)
  await voice_client.disconnect()

keep_alive()
bot.run(token)
