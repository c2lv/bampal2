import discord, os, random, crawling, aiocron
from discord.ext import commands
import load_secrets as secrets

# stream = discord.Streaming(name="", url=""))
# listen = discord.Activity(type=discord.ActivityType.listening, name="")
# watch = discord.Activity(type=discord.ActivityType.watching, name=""))
game = discord.Game("열심히 공지사항 정리")
prefix = "!"
win_straight = 0 # 연승 횟수

# Get discord token
token = os.environ.get('discord_token')

# notice types
type_general = "일반"
type_academic = "학사"
type_scholarship = "장학"

# notice links
general_url = "https://www.dongguk.edu/article/GENERALNOTICES/list"
academic_url = "https://www.dongguk.edu/article/HAKSANOTICE/list"
scholarship_url = "https://www.dongguk.edu/article/JANGHAKNOTICE/list"

# discord channel id
ch_general_id = 953744824954138675
ch_academic_id = 953741410434175016
ch_scholarship_id = 953741442717732944

bot = commands.Bot(command_prefix=prefix, status=discord.Status.online, activity=game)

'''
Loop
'''
class PostNotice(commands.Cog):
    @aiocron.crontab('0 18 * * *') # minute hour day month week second
    async def postNotice():
        # Get channel
        ch_general = bot.get_channel(ch_general_id)
        ch_academic = bot.get_channel(ch_academic_id)
        ch_scholarship = bot.get_channel(ch_scholarship_id)

        # Get notice
        general_message = crawling.run(general_url, type_general)
        academic_message = crawling.run(academic_url, type_academic)
        scholarship_message = crawling.run(scholarship_url, type_scholarship)

        # Send message to channel
        await ch_general.send(general_message)
        await ch_academic.send(academic_message)
        await ch_scholarship.send(scholarship_message)

class TestPost(commands.Cog):
    @aiocron.crontab('0 * * * *') # minute hour day month week second
    async def postNotice():
        # Get channel
        ch_general = bot.get_channel(954219950183170138)
        ch_academic = bot.get_channel(954219997121638420)
        ch_scholarship = bot.get_channel(954220024774688818)

        # Send message to channel
        await ch_general.send("1시간 경과")
        await ch_academic.send("1시간 경과")
        await ch_scholarship.send("1시간 경과")

bot.add_cog(PostNotice(bot))
bot.add_cog(TestPost(bot))

'''
Events
'''
# @bot.event

'''
Commands
'''
@bot.command(aliases=['안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')

@bot.command(aliases=['앵무새'])
async def repeat(ctx, *, txt):
    await ctx.send(txt)

@bot.command(aliases=['주사위', 'dice'])
async def roll(ctx, number = 6):
    await ctx.send(f'떼구르르... 주사위를 굴려 {random.randint(1, int(number))}이(가) 나왔습니다. (1~{number})')
@roll.error
async def roll_error(ctx, error):
    await ctx.send('올바른 명령어가 아닙니다.\n(N면체 주사위를 굴리고 싶을 때: !roll N)')

@bot.command(aliases=['사다리', '사다리타기', '사다리게임'])
async def ladder(ctx, number:int, *member:str):
    txt = ""
    result = random.sample(member, number)
    for i in result:
        txt = txt + i + " "
    await ctx.send(txt + "당첨!")
@ladder.error
async def ladder_error(ctx, error):
    await ctx.send('올바른 명령어가 아닙니다.\n(3명 중 N명을 뽑는 사다리게임을 하고 싶을 때: !ladder N 사람1 사람2 사람3)')

@bot.command(aliases=['개발자'])
async def developer(ctx):
    await ctx.send('밤팔이 봇의 개발자는 c2lv입니다.\n개발자의 깃허브와 블로그에 놀러오세요!\n깃허브: https://github.com/c2lv\n네이버 블로그: https://blog.naver.com/hyeonjun7')

@bot.command(aliases=['가위바위보'])
async def rps(ctx, hand:str):
    global win_straight
    rock = ["rock", "묵", "바위", "주먹"]
    scissors = ["scissors", "찌", "가위"]
    paper = ["paper", "빠", "보", "보자기"]
    hands = ["바위", "가위", "보"]
    if (hand not in rock) and (hand not in scissors) and (hand not in paper):
        await ctx.send("뭘 내셨는지 모르겠어요! 다시 내주세요.")
    else:
        bot_choice = random.choice(hands)
        if (hand in rock and bot_choice == hands[1]) or (hand in scissors and bot_choice == hands[2]) or (hand in paper and bot_choice == hands[0]):
            win_straight += 1
            await ctx.send(f"{bot_choice}!\n{ctx.author}가 이겼습니다!\n현재 {win_straight}연승!")
        else:
            win_straight = 0
            if (hand in rock and bot_choice == hands[0]) or (hand in scissors and bot_choice == hands[1]) or (hand in paper and bot_choice == hands[2]):
                await ctx.send(f"{bot_choice}!\n비겼습니다.")
            if (hand in rock and bot_choice == hands[2]) or (hand in scissors and bot_choice == hands[0]) or (hand in paper and bot_choice == hands[1]):
                await ctx.send(f"{bot_choice}!\n밤팔이가 이겼습니다!")

@bot.command(aliases=['도움', '도움말', '밤팔이'])
async def h(ctx):
    embed = discord.Embed(title="밤팔이", description="평일 오후 6시마다 그날 올라온 동국대학교의 일반/학사/장학공지를 알려주는 재주 많은 동국대공지맨!", color=0xf76300)
    embed.add_field(name="1. 인사", value="!hello", inline=False)
    embed.add_field(name="2. 앵무새", value="!repeat [따라할 말]", inline=False)
    embed.add_field(name="3. 주사위", value="!roll [범위 숫자]", inline=False)
    embed.add_field(name="4. 사다리게임", value="!ladder [당첨자 수] [사람 1] [사람 2] [사람 3] [...]", inline=False)
    embed.add_field(name="5. 가위바위보", value="!rps [가위/바위/보]", inline=False)
    embed.add_field(name="6. 개발자", value="!developer", inline=False)
    await ctx.send(embed=embed)

'''
Runs
'''
bot.run(secrets.get_token())
bot.run(token) # run의 인자로 token 입력
