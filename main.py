#Imports / Импортируем всякое
import os
import sys
import discord
from discord.ext import commands
from discord.ui import Button, View
import logging
import datetime
import threading

from config import settings



intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.listening, name="стоны")
client = commands.Bot(command_prefix='$', intents=intents)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')



# Статус: Включен
@client.event
async def on_ready():
    embed=discord.Embed(title="Статус: Включен",
                        description="Бот включен и готов к функционированию",
                        color=0x33ff55,
                        timestamp=datetime.datetime.now())
    embed.set_thumbnail(url="https://img.icons8.com/?size=256&id=VFaz7MkjAiu0&format=png")
    channel = client.get_channel(1290761574306545706)
    await channel.send(embed=embed)
    await client.change_presence(activity=activity)

@client.event
async def on_member_join(member):
    channel = 1292227488109301782

    embed = discord.Embed(
        title=f'WELCOME, {member.mention}!',
        color=0x5ffdff
    )
    embed.set_author(icon_url=member.avatar_url)
    embed.set_footer(text=f'Ваш ID: {member.id} • {datetime.datetime.now()}')

    await channel.send(embed=embed)

@client.event
async def on_message(message):
    banwords = ['pidor']
    channel = client.get_channel(1292227488109301782)
    client_author = client.get_user(int(1238954471577620482))
    if client.user in message.mentions:
        embed = discord.Embed(title="Справка",
                              color=0x3c2f2f,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url='https://i.ibb.co/c8Fgy2j/photo-2024-10-03-19-13-07.jpg')
        embed.add_field(name="ЯП: ", value="Python", inline=True)
        embed.add_field(name="Создатель: ", value=f'<@{1238954471577620482}>', inline=True)
        embed.add_field(name="Github: ", value="[<клик>](https://github.com/CrimsonCoalition/CrimsonEye)", inline=False)
        await channel.send(embed=embed)
    await client.process_commands(message)


# Вызов справки
@client.event
async def on_message(message):
    banwords = ['pidor']
    channel = client.get_channel(1290761574306545706)
    if client.user in message.mentions:
        embed = discord.Embed(title="Справка",
                              color=0x3c2f2f,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=rliRb6nC38ip&format=png&color=000000")
        embed.add_field(name="ЯП: ", value="Python", inline=True)
        embed.add_field(name="Создатель: ", value="@salø", inline=True)
        embed.add_field(name="Github: ", value="-", inline=False)
        await channel.send(embed=embed)
    await client.process_commands(message)

    if message.author.id == 1290760952496525456:
        return
    else:
        for word in banwords:
            if word in message.content.lower():
                author = message.author
                embed = discord.Embed(title="Обнаружен банворд",
                                      color=0xfffc2c,
                                      timestamp=datetime.datetime.now())
                embed.set_thumbnail(url="https://img.icons8.com/?size=100&id=rliRb6nC38ip&format=png&color=000000")
                embed.add_field(name="Пользователь", value=f"{author.mention}", inline=False)
                embed.add_field(name="Канал", value=f"{message.channel.mention}", inline=False)
                embed.add_field(name="Текст сообщения", value=f"{message.content}", inline=False)
                embed.add_field(name="Банворд", value=f"{word}", inline=False)
                embed.set_footer(text=f"ID сообщения: {message.id}", icon_url="https://img.icons8.com/?size=256&id=63308&format=png")
                await channel.send(embed=embed)
    await client.process_commands(message)

# Статус: Выключен
@client.command()
async def shutdown(channel):
    embed1=discord.Embed(title="Статус: Выключен",
                         description="Бот прервал соединение c дискордом и выключился",
                         color=0xff2a2a,
                         timestamp=datetime.datetime.now())
    embed1.set_thumbnail(url="https://img.icons8.com/?size=256&id=OZuepOQd0omj&format=png")
    channel = client.get_channel(1290761574306545706)
    await channel.send(embed=embed1)
    await client.close()

#Статус: Перезагрузка
@client.command()
async def restart(ctx):
    if ctx.channel.id == 1290761574306545706:
        embed = discord.Embed(title="Статус: Перезагрузка...",
                              description="В скором времени бот включится и продолжит работать в обычном режиме",
                              color=0x05aab0, timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://img.icons8.com/?size=256&id=bDkQlpOV2TWB&format=png")
        await ctx.send(embed=embed)
        os.execv(sys.executable, ['python'] + sys.argv)





client.run(settings['token'])
