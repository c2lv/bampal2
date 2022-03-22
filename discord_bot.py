import discord, os, random, crawling, aiocron, const
from discord.ext import commands
from datetime import datetime

# stream = discord.Streaming(name="", url=""))
# listen = discord.Activity(type=discord.ActivityType.listening, name="")
# watch = discord.Activity(type=discord.ActivityType.watching, name=""))
game = discord.Game("열심히 공지사항 정리")
win_straight = 0 # 연승 횟수

# Get discord token
token = os.environ.get('BOT_TOKEN')

bot = commands.Bot(command_prefix=const.PREFIX, status=discord.Status.online, activity=game)

'''
Loops
'''
class PostNotice(commands.Cog):
    @aiocron.crontab('0 9 * * *') # minute hour day month week second, UTC
    async def postNotice():
        # Get channel
        ch_general = bot.get_channel(const.CH_GENERAL_ID)
        ch_academic = bot.get_channel(const.CH_ACADEMIC_ID)
        ch_scholarship = bot.get_channel(const.CH_SCHOLARSHIP_ID)
        ch_workScholarship = bot.get_channel(const.CH_WORKSCHOLARSHIP_ID)
        ch_collegeOfEducation = bot.get_channel(const.CH_COLLEGEOFEDUCATION_ID)

        # Get notice
        general_message = crawling.run(const.GENERAL_URL, const.TYPE_GENERAL)
        academic_message = crawling.run(const.ACADEMIC_URL, const.TYPE_ACADEMIC)
        scholarship_message = crawling.run(const.SCHOLARSHIP_URL, const.TYPE_SCHOLARSHIP)
        workScholarship_message = crawling.run(const.WORKSCHOLARSHIP_URL, const.TYPE_WORKSCHOLARSHIP)
        collegeOfEducation_message = crawling.run(const.COLLEGEOFEDUCATION_URL, const.TYPE_COLLEGEOFEDUCATION)

        # Send message to channel
        await ch_general.send(general_message)
        await ch_academic.send(academic_message)
        await ch_scholarship.send(scholarship_message)
        await ch_workScholarship.send(workScholarship_message)
        await ch_collegeOfEducation.send(collegeOfEducation_message)

bot.add_cog(PostNotice(bot))

'''
Events
'''
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("띠용? 무슨 말씀이신지 잘 모르겠어요. 제가 모르는 명령어를 쓰신 것은 아닌가요?\n`!밤팔이`를 입력하시면 사용 가능한 명령어와 사용 방법을 확인하실 수 있습니다.")
# @bot.event
# async def on_ready():
#     pass

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
    if isinstance(error, commands.BadArgument):
        await ctx.send("정수를 입력해주세요!")

@bot.command(aliases=['사다리', '사다리타기', '사다리게임'])
async def ladder(ctx, number:int, *member:str):
    txt = ""
    if number == 0:
        await ctx.send("0명을 뽑으면 아무도 당첨되지 않아요...")
    else:
        result = random.sample(member, number)
        for i in result:
            txt = txt + i + " "
        await ctx.send(txt + "당첨!")
@ladder.error
async def ladder_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("명령어만 쓴 것은 아닌지 확인해주세요!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("당첨자 수는 정수를 입력해주세요!")
    else:
        await ctx.send("당첨자 수보다 사람이 적은 것은 아닌지 확인해주세요!")

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
@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("낼 것을 입력해주세요!")

@bot.command(aliases=['도움', '도움말', '밤팔이'])
async def h(ctx):
    embed = discord.Embed(title=":chestnut: 밤팔이", description="오후 6시마다 그날 올라온 동국대 공지를 알려주는 재주 많은 동국대공지맨!\n사용가능한 명령어와 사용 방법은 !help, !help [명령어]로도 확인할 수 있습니다.", color=0xf76300)
    embed.add_field(name="1. 인사", value="!hello", inline=False)
    embed.add_field(name="2. 앵무새", value="!repeat [따라할 말]", inline=False)
    embed.add_field(name="3. 주사위", value="!roll [범위 숫자]", inline=False)
    embed.add_field(name="4. 사다리게임", value="!ladder [당첨자 수] [사람 1] [사람 2] [사람 3] [...]", inline=False)
    embed.add_field(name="5. 가위바위보", value="!rps [가위/바위/보]", inline=False)
    embed.add_field(name="6. 개발자", value="!developer", inline=False)
    embed.add_field(name="7. 서버시간확인", value="!st", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['서버시간확인'])
async def st(ctx):
    now = datetime.now()
    await ctx.send(now)
    await ctx.send(f"현재 서버 시간은 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초입니다.")

'''
Run
'''
bot.run(token)
