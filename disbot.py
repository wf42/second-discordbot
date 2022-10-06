import discord
from discord.ext import commands
import os
import random
import asyncio
from keep_alive import keep_alive

client = commands.Bot(command_prefix = os.getenv('PREFIX'))
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' hi'))
    print('im online!') 


@client.command()
async def ping(ctx):
    await ctx.send(f'**> Bot latency {round(client.latency * 1000)}ms**')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        myem=discord.Embed(title ='error', description ='ليس لديك الصلاحيه', color=0x0FF0000)
        await ctx.send(embed=myem , delete_after=2)

@client.command()
@commands.has_permissions(manage_messages=True)
async def cl(ctx, amount=80):
    await ctx.channel.purge(limit=amount)
    myem1=discord.Embed(title ='Done', description ='تم حذف 80 من الرسائل', color=0x00FF00)
    await ctx.send(embed=myem1 , delete_after=1)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason = 'لا يوجد سبب مكتوب'):
        await member.kick(reason=reason)
        kickem=discord.Embed(title ='تم طرد العضو', description =reason, color=0x00FF00)
        await ctx.send(embed=kickem , delete_after=2)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason = 'لا يوجد سبب مكتوب'):
        await member.ban(reason=reason)
        banem=discord.Embed(title ='تم تبنيد العضو', description =reason, color=0x00FF00)
        await ctx.send(embed=banem, delete_after=2)

@client.command()
@commands.has_permissions(manage_messages = True)
async def say(ctx, saymag=None):
  if saymag == None:
    return await ctx.send('لازم تقولي الكلمات', delete_after=2)
  sayem = discord.Embed(title = f"{ctx.author}", description = f"{saymag}")
  await ctx.send(embed=sayem)


@client.command()
async def avatar(ctx,member : discord.Member = None):
  if member == None:
    member = ctx.author

  memberAvatar=member.avatar_url

  avem=discord.Embed(title = f"{member.name} avatar")
  avem.set_image(url = memberAvatar)
  avem.set_footer(icon_url = ctx.author.avatar_url, text = f"{ctx.author}")
  await ctx.send(embed=avem)
 
@client.command()
async def ايه(ctx):
  a1 = ["﴿لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا ۖ﴾" ,"﴿يَا أَيُّهَا الَّذِينَ آمَنُوا اذْكُرُوا اللَّهَ ذِكْرًا كَثِيرًا﴾" ,"﴿وَلَا تَخَافِي وَلَا تَحْزَنِي﴾"]
  await ctx.reply(random.choice(a1))
  await asyncio.sleep(300)


keep_alive()
client.run(os.getenv('TOKEN'))
