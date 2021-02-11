import discord
from discord.ext import commands
from discord import utils
import asyncio
from config import settings
import json

settings = {
    'token': 'ODAyOTQ1OTc4MDQ2ODczNjcy.YA2ntw.0ntrS1rHnvOgd7UO3JxNvIuNgPE',
    'bot': 'python',
    'id': 802945978046873672,
    'prefix': '!'
}

client = discord.Client()
bot = commands.Bot(command_prefix = settings['prefix'])



@bot.command() 
async def Повтори(ctx,arg): 
    await ctx.send(arg)  #Повторяшка
@bot.command() 
async def повтори(ctx,arg): 
    await ctx.send(arg)  #Повторяшка2


@bot.command()
async def привет(ctx):
    await ctx.send(f'Привет') #Привет
@bot.command()
async def Привет(ctx):
    await ctx.send(f'Привет') #Привет2


@bot.command()
async def Правила(ctx):
    await ctx.send(f'Слышь! Не кидай бумагу в унитаз, кидай в ведро епта!') #Правила
@bot.command()
async def правила(ctx):
    await ctx.send(f'Их нету') #Правила2


@bot.command() #профиль
async def Профиль(ctx,member:discord.Member):
    emb = discord.Embed(title="Информация о пользователе",color=0xff0000)
    emb.add_field(name='Когда присоединился:',value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name='Когда был создан аккаунт:',value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"))
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f'Вызвано:{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)
@bot.command() #профиль 2
async def профиль(ctx,member:discord.Member):
    emb = discord.Embed(title="Информация о пользователе",color=0xff0000)
    emb.add_field(name='Когда присоединился:',value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name='Когда был создан аккаунт:',value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"))
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f'Вызвано:{ctx.message.author}',icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def Mute(ctx,member:discord.Member,time:int,reason):
    channel = bot.get_channel(807312848912777267)
    muterole = discord.utils.get(ctx.guild.roles,name='Muted')
    emb = discord.Embed(title='Выдан Mute',color=0xff0000)
    emb.add_field(name='Администратор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Обвиненный',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    emb.add_field(name='Время в секундах',value=time,inline=False)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await asyncio.sleep(time)
    await member.remove_roles(muterole)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def UnMute(ctx,member:discord.Member):
    channel = bot.get_channel(807312848912777267)
    muterole = discord.utils.get(ctx.guild.roles,name='Muted')
    emb = discord.Embed(title='Выдан UnMute',color=0xff0000)
    emb.add_field(name='Администратор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Освобожденный',value=member.mention,inline=False)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def Kick(ctx,member:discord.Member,reason):
    channel = bot.get_channel(807312848912777267)
    emb = discord.Embed(title='Выдан Kick',color=0xff0000)
    emb.add_field(name='Администратор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Наказанный',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.kick()
    await channel.send(embed = emb)


@bot.command()
@commands.has_permissions(view_audit_log=True)
async def Ban(ctx,member:discord.Member,reason):
    channel = bot.get_channel(807312848912777267)
    emb = discord.Embed(title='Выдан BAN',color=0xff0000)
    emb.add_field(name='Администратор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Наказанный',value=member.mention,inline=False)
    emb.add_field(name='Причина',value=reason,inline=False)
    await member.ban()
    await channel.send(embed = emb)
    
    
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def Clear(ctx,amount=1000):
    deleted = await ctx.message.channel.purge(limit=amount + 1)

@bot.command()
@commands.has_permissions(view_audit_log=True)
async def clear(ctx,amount=1000):
    deleted = await ctx.message.channel.purge(limit=amount + 1)
    
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(807544680904261633)
    for guild in bot.guilds:
        newrole = discord.utils.get(guild.roles,id=807318612913815583)
        await member.add_roles(newrole)
        await channel.send(f'{member.mention} Добро пожаловать!')
        

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(807544680904261633)
    await channel.send(f'{member} Покинул нас!')


@bot.event
async def on_message (message): 

    with open('C:\\Users\\Nekore\\Desktop\\Python\\lvl.json','r') as f:
        users = json.load(f)
    async def update_data(users,user):
        if not user in users:
            users[user] = {}
            users[user]['exp'] = 0
            users[user]['lvl'] = 1
    async def add_exp(users,user,exp):
        users[user]['exp'] += exp
    async def add_lvl(users,user):
        exp = users[user]['exp']
        lvl = users[user]['lvl']
        if exp > lvl:
            await message.channel.send(f'{message.author.mention} повысил свой уровень!')
            users[user]['exp'] = 0
            users[user]['lvl'] = lvl + 1
            lvl = lvl + 1
    await update_data(users,str(message.author.id))
    await add_exp(users,str(message.author.id),0.1)
    await add_lvl(users,str(message.author.id))
    with open('C:\\Users\\Nekore\\Desktop\\Python\\lvl.json','w') as f:
        json.dump(users,f)
        await bot.process_commands(message)

        

@bot.event
async def on_ready():
    print(f"Ready!")
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game('I love BOTS<3'))

@bot.command()
async def Команды(ctx):
  emb = discord.Embed(title="Команды",discription='Учитывайте регистер!',color=0xff0000)
  emb.add_field(name='Для администрации',value=f'1- !Ban  @пользователь\n 2- !Kick  @пользователь  Причина\n3- !Mute  @пользователь  Время в секундах  Причина\n4- !UnMute  @пользователь\n5- !Clear  Число')
  emb.add_field(name='Основные',value=f'1- !Привет  \n2- !Повтори текст\n3- !Команды  \n4- !Профиль  ')
  
  await ctx.send(embed = emb)

@bot.command()
async def команды(ctx):
  emb = discord.Embed(title="Команды",description='Учитывайте регистер!',color=0xff0000)
  emb.add_field(name='Для администрации',value=f'1- !Ban  @пользователь\n 2- !Kick  @пользователь  Причина\n3- !Mute  @пользователь  Время в секундах  Причина\n4- !UnMute  @пользователь\n5- !Clear  Число')
  emb.add_field(name='Основные',value=f'1- !Привет  \n2- !Повтори текст\n3- !Команды  \n4- !Профиль  ')
  await ctx.send(embed = emb)







bot.run(settings['token'])