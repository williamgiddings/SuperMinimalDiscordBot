from discord.ext import commands
import config
import discord

#------------------------------------------------------------------------------

cfg = config.load_config()
bot = commands.Bot(command_prefix=cfg['prefix'], description=cfg['description'], intents=discord.Intents.all())
COGS = [] # drop your cogs here! check out my github for some cool ones or use my stub cog to make your own

#------------------------------------------------------------------------------

def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot

#------------------------------------------------------------------------------
        
@bot.event
async def on_ready():

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# ------------------------------------------------------------------------------

add_cogs(bot)
bot.run(cfg['token'])