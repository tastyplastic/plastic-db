import hypixel
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import urbandictionary as ud

bot = commands.Bot(command_prefix='~')
API_KEYS = ['']
hypixel.setKeys(API_KEYS)

# help
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Color.purple())
    embed.set_author(name='help')
    embed.add_field(name='lvl', value='hypixel player level', inline=False)
    embed.add_field(name='ud', value='urban dictionary', inline=False)

    await ctx.send(embed=embed)


# Player Level
@bot.command()
async def lvl(ctx, username):
    player = hypixel.Player(username)
    HyLevel = str(player.getLevel())
    await ctx.send("```" + str(username) + "'s level is > " + str(HyLevel) + "```")

# UrbanDictionary
@bot.command()
async def ud(ctx):
    rand = ud.random()
    for things in rand:
        thing = str(things)
        await ctx.send("```" + thing + "```")
        break



bot.run('')
