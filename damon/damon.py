from multiprocessing import AuthenticationError
import discord
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")
DiscordComponents(bot)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help | Marvel Support"))
    print(bot.user.name, "is Ready..!")

@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title = 'All Commands List',
        description = '<a:dotmrn:969495438061350932> Prefix `.`',
        color = discord.Colour.random(),
    )
    embed.add_field(name='<a:zy1:764943664098836550> Main Commands List', value='`.heyo` `.custombot` `.premium` ')
    embed.set_footer(text='Made with 💖 by Serious Wolfey#9377')
    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def heyo(ctx):
    await ctx.reply('Hello..! I am Damon. How can i help you ? ')


@bot.command()
async def custombot(ctx,*, user = discord.Member):
    embed = discord.Embed(
        title = 'Custom Bot Rates',
        description = '**All Rates of Custom Bots**',
        color = discord.Colour.gold(),
    )
    embed.add_field(name='<a:op11:764200185253199892> __Moderation bot__', value='**<a:arrow:969869074408558592> 120/month   800/year**', inline=False)
    embed.add_field(name='<a:em:764943862677635102> __Security__', value='**<a:arrow:969869074408558592> 160/month    1200/year**', inline=False)
    embed.add_field(name='<:automod:969230660176859156> __Auto Moderation__', value='**<a:arrow:969869074408558592> 140/month   900/year**', inline=False)
    embed.add_field(name='<a:MusiC:764240569723387934> __Music__', value='**<a:arrow:969869074408558592> 120/month  850/year**', inline=False)
    embed.add_field(name='<a:Nikeemoji:764200430737031168> __Combination__', value='**<a:arrow:969869074408558592> 250/month 2800/year**', inline=False)
    embed.add_field(name='<:welcome:969261482573459497> __Welcomer__', value='<a:arrow:969869074408558592> **150₹ addition charges 30₹/month & 250₹/yearly**', inline=False)
    embed.add_field(name='<a:roles:969262177422811226>__Selfrole__', value='<a:arrow:969869074408558592> **180₹ addition charges 40₹/month & 300₹/yearly**', inline=False)
    embed.add_field(name='<a:OTHER:969269578809102366> __Other Features__', value='<a:arrow:969869074408558592> **₹100/charges & ₹30 monthly & ₹250 yearly**', inline=False)
    embed.set_footer(text='Made with 💖 by Serious Wolfey#9377', icon_url= ctx.author.avatar_url)
    embed.set_author(name= ctx.author.name, icon_url= ctx.author.avatar_url)
    embed.set_thumbnail(url = ctx.author.avatar_url)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('<:marvel:969871179353583687>')

@bot.command()
async def premium(ctx,*, user = discord.Member):
    embed = discord.Embed(
        title = 'Marvel Prime',
        description = '<@743484920437145601> is premium version of <@748583869527097376>',
        color = discord.Colour.gold(),
    )
    embed.add_field(name='<:m_prime_logo:949016884626489424> **Buy Marvel Premium**', value='[Click Here To Buy](https://www.marvelbot.tk/)')
    embed.add_field(name='<:support:969917272669966397> **SUPPORT**', value='[marvel.gg/support](https://discord.gg/Qj8VKuReBu)')
    embed.set_footer(text='Made with 💖 by Serious Wolfey#9377', icon_url= 'https://cdn.discordapp.com/avatars/757184713390686208/d96b433913f36d1e7d717f963b623548.webp?size=2048')
    await ctx.send(embed=embed)

bot.run("OTY5MTM4NzUxNDU0NDc4MzU2.YmpCzA.x43SWAGydGJu4mVxhFGXO3WD5n4")