import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


@bot.command(name='search')
async def search_messages(ctx, user_mention):
  print(f"User Mention: {user_mention}")

  # Extract user ID from mention
  try:
    print(f"User ID: {user_mention}")
    user_id = int(user_mention[2:-1])
    print(f"User ID: {user_id}")
  except ValueError:
    return await ctx.send("Invalid user mention format.")

  # Get the user object
  target_user = bot.get_user(user_id)

  if target_user is None:
    return await ctx.send("User not found.")

  # Search messages in the channel for the specified user and query
  messages = []
  async for message in ctx.channel.history(limit=None):
    if message.author == target_user:
      messages.append(message)

  if messages:
    await ctx.send(f'Total messages found: {len(messages)}')
  else:
    await ctx.send(
        f"No messages found from {target_user.name} with the specified query.")


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run(os.environ['TOKEN'])
