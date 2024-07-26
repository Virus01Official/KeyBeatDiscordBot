import discord
import os
from discord.ext import commands

# Set up the bot and intents
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Define the announcement channel ID and the announcement role ID
ANNOUNCEMENT_CHANNEL_ID = 1208377063870824458  # Replace with the actual channel ID
ANNOUNCEM_CHANNEL_ID = 1208377024981237801  # Replace with the actual channel ID
ANNOUNCEMENT_ROLE_ID = 1208379129523605584  # Replace with the actual role ID you want to mention

@bot.command()
async def feedback(ctx, *, user_feedback: str):
    # Replace 'your_feedback_channel_id' with the actual channel ID where you want to receive feedback
    feedback_channel = bot.get_channel(1262021731292418119)

    if feedback_channel:
        await feedback_channel.send(f"New feedback from {ctx.author.mention}:\n{user_feedback}")
        await ctx.send("Thank you for your feedback! It has been submitted.")
    else:
        await ctx.send("Feedback channel not found. Please set up a valid feedback channel.")

@bot.command()
@commands.has_permissions(administrator=True)  # Check if the user has Administrator permissions
async def announce(ctx, *, message: str):
    announcement_channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
    announcement_role = ctx.guild.get_role(ANNOUNCEMENT_ROLE_ID)  # Get the role object

    if announcement_channel:
        if announcement_role:
            # Mention the role and send the announcement message
            await announcement_channel.send(f"{announcement_role.mention} {message}")
            await ctx.send("Announcement has been sent.")
        else:
            await ctx.send("Announcement role not found. Please set up a valid role.")
    else:
        await ctx.send("Announcement channel not found. Please set up a valid announcement channel.")

# Handle permission error
@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")

@bot.command()
@commands.has_permissions(administrator=True)  # Check if the user has Administrator permissions
async def announcement(ctx, *, message: str):
    announcement_channel = bot.get_channel(ANNOUNCEM_CHANNEL_ID)
    announcement_role = ctx.guild.get_role(ANNOUNCEMENT_ROLE_ID)  # Get the role object

    if announcement_channel:
        if announcement_role:
            # Mention the role and send the announcement message
            await announcement_channel.send(f"{announcement_role.mention} {message}")
            await ctx.send("Announcement has been sent.")
        else:
            await ctx.send("Announcement role not found. Please set up a valid role.")
    else:
        await ctx.send("Announcement channel not found. Please set up a valid announcement channel.")

# Handle permission error
@announcement.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")

# Run the bot
bot.run(my_secret)
