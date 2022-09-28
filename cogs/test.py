from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command(aliases=['테스트'])
    async def test(self, ctx):
        await ctx.send('테스트 명령어를 실행하셨습니다.')

async def setup(bot: commands.Bot):
    await bot.add_cog(Test(bot))