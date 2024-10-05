import os
import sys
import discord
from discord.ext import commands
from discord.ui import Button, View
import logging
import datetime
import threading




intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.listening, name="стоны")
client = commands.Bot(command_prefix='$', intents=intents)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')




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


@client.command()
async def restart(ctx):
    if ctx.channel.id == 1290761574306545706:
        embed = discord.Embed(title="Статус: Перезагрузка...",
                              description="В скором времени бот включится и продолжит работать в обычном режиме",
                              color=0x05aab0, timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://img.icons8.com/?size=256&id=bDkQlpOV2TWB&format=png")
        await ctx.send(embed=embed)
        os.execv(sys.executable, ['python'] + sys.argv)





client.run('MTI5MDc2MDk1MjQ5NjUyNTQ1Ng.GeMLJ3.tncG6DJbGfSRuZYzMuti7tH2S7GQl_dQTy6an0', log_handler=handler)