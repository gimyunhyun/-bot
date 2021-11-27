import discord
import os
from discord.ext import commands
bot = commands.Bot(command_prefix='$')
access_token = os.environ['BOT_TOKEN']
TOKEN = 'access_token'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('$명령어'))
    print('성공적으로 구동되었습니다.]')

        
import asyncio, discord
from discord.ext import commands

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}ㅎㅇㅎㅇ')


@bot.command()
async def 삭제(ctx):
    await ctx.message.delete()
    await ctx.channel.send('메시지를 삭제했습니다.')
    

@bot.command()
async def 주사위(ctx):
    import random
    randnum = random.randint(1, 6)  # 1이상 6이하 랜덤 숫자를 뽑음
    await ctx.send(f'주사위 결과는 {randnum} 입니다.')

@bot.command()
async def 음식추천(ctx):
    import random
    await ctx.trigger_typing()
    randomNum = random.randrange(1, 17)
    if randomNum == 1:
        await ctx.send(f'{ctx.message.author.mention}마라탕을 드시는게 좋을것같습니다.')
    if randomNum == 2:
        await ctx.send(f'{ctx.message.author.mention}초밥을 드시는게 좋을것같습니다.')
    if randomNum == 3:
        await ctx.send(f'{ctx.message.author.mention}피자를 드시는게 좋을것같습니다.')
    if randomNum == 4:
        await ctx.send(f'{ctx.message.author.mention}햄버거를 드시는게 좋을것같습니다.')
    if randomNum == 5:
        await ctx.send(f'{ctx.message.author.mention}드시지 마시고 다이어트하세요.')
    if randomNum == 6:
        await ctx.send(f'{ctx.message.author.mention}치킨을 드시는게 좋을것같습니다.')
    if randomNum == 7:
        await ctx.send(f'{ctx.message.author.mention}떡볶이를 드시는게 좋을것같습니다.')
    if randomNum == 8:
        await ctx.send(f'{ctx.message.author.mention}볶음밥을 드시는게 좋을것같습니다.')
    if randomNum == 9:
        await ctx.send(f'{ctx.message.author.mention}중식을 드시는게 좋을것같습니다.')
    if randomNum == 10:
        await ctx.send(f'{ctx.message.author.mention}그만먹고 다이어트하십시요.')
    if randomNum == 11:
        await ctx.send(f'{ctx.message.author.mention}튀김류를 드시는게 좋을것같습니다.')
    if randomNum == 12:
        await ctx.send(f'{ctx.message.author.mention}라면류를 드시는게 좋을것같습니다.')
    if randomNum == 13:
        await ctx.send(f'{ctx.message.author.mention}고기류를 드시는게 좋을것같습니다.')
    if randomNum == 14:
        await ctx.send(f'{ctx.message.author.mention}채소류를 드시는게 좋을것같습니다.')
    if randomNum == 15:
        await ctx.send(f'{ctx.message.author.mention}오늘은 밀가류 종류를 드시는게 좋을것같습니다.')
    if randomNum == 16:
        await ctx.send(f'{ctx.message.author.mention}드시지마십시요.')


@bot.command()
async def 운(ctx):
    import random
    await ctx.trigger_typing()
    randomNum = random.randrange(1, 12)
    if randomNum == 1:
        await ctx.send(f'{ctx.message.author.mention}님은 모든일이 선두가 됨으로 리더역할을 잘해야합니다.')
    if randomNum == 2:
        await ctx.send(f'{ctx.message.author.mention}님은 슬픈일이있을 예정입니다.')
    if randomNum == 3:
        await ctx.send(f'{ctx.message.author.mention}님은 오늘 행복한일이 나타날껍니다.')
    if randomNum == 4:
        await ctx.send(f'{ctx.message.author.mention}님은 행동을 조심해야 합니다.')
    if randomNum == 5:
        await ctx.send(f'{ctx.message.author.mention}님은 자책하지 마시고 주저하지마시고 앞을보고 달려가세요.')
    if randomNum == 6:
        await ctx.send(f'{ctx.message.author.mention}님은 백발백중 모든것이 명중하는것처럼 모든일이 술술 풀릴껍니다.')
    if randomNum == 7:
        await ctx.send(f'{ctx.message.author.mention}님은 엄청난 행운이 올것입니다 본인의 실수로 행운이 날라갈수있어 조심하게 행동해주세요.')
    if randomNum == 8:
        await ctx.send(f'{ctx.message.author.mention}님은 친구들에게 갈굼을 당하지만 그기억은 좋은기억으로 남을겁니다.')
    if randomNum == 9:
        await ctx.send(f'{ctx.message.author.mention}님은 엄청난불행이 올것입니다.')
    if randomNum == 10:
        await ctx.send(f'{ctx.message.author.mention}님은 오늘 하루가 힘들게 느껴질겁니다 지금부터 어떤 고난이 와도 자기 자신을 존중할줄알아야합니다.')
    if randomNum == 11:
        await ctx.send(f'{ctx.message.author.mention}님은 오늘 하루가 찜찜하실껍니다.')
    if randomNum == 12:
        await ctx.send(f'{ctx.message.author.mention}모든일이 행운이고 행복하고 좋은일만 나타날 껍니다.')

@bot.command()
async def 바보(ctx):
    import random
    await ctx.trigger_typing()
    randomNum = random.randrange(1, 12)
    if randomNum == 1:
        await ctx.send(f'{ctx.message.author.mention}윤현이가 제일 바보입니다.')
    if randomNum == 2:
        await ctx.send(f'{ctx.message.author.mention}민서가 제일 바보입니다.')
    if randomNum == 3:
        await ctx.send(f'{ctx.message.author.mention}찬영이가 제일 바보입니다.')
    if randomNum == 4:
        await ctx.send(f'{ctx.message.author.mention}상섭이가 제일 바보입니다.')
    if randomNum == 5:
        await ctx.send(f'{ctx.message.author.mention}현우가 제일 바보입니다.')
    if randomNum == 6:
        await ctx.send(f'{ctx.message.author.mention}건형이가 제일 바보입니다.')
    if randomNum == 7:
        await ctx.send(f'{ctx.message.author.mention}태수가 제일 바보입니다.')
    if randomNum == 8:
        await ctx.send(f'{ctx.message.author.mention}소원님이 제일 바보입니다.')
    if randomNum == 9:
        await ctx.send(f'{ctx.message.author.mention}우진이가 제일 바보입니다.')
    if randomNum == 10:
        await ctx.send(f'{ctx.message.author.mention}지민이가 제일 바보입니다 .')
    if randomNum == 11:
        await ctx.send(f'{ctx.message.author.mention}건우가 제일 바보입니다.')
    if randomNum == 12:
        await ctx.send(f'{ctx.message.author.mention}성용이가 제일 바보입니다.')
    if randomNum == 13:
        await ctx.send(f'{ctx.message.author.mention}제혁이가 제일 바보입니다.')
    if randomNum == 14:
        await ctx.send(f'{ctx.message.author.mention}현덕이가 제일 바보입니다.')
    if randomNum == 15:
        await ctx.send(f'{ctx.message.author.mention}준영이가 제일 바보입니다.')

@bot.command()
async def 초대(ctx):
    await ctx.channel.send(f'https://discord.gg/zgTw5pgPQG')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다.")

bot.run(TOKEN)
