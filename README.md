# 밤팔이
:elephant: [채널 입장하기](https://discord.gg/6BVxgEvCM7)  
![bampal2_app_icon](./bampal2.png)

매일 오후 6시마다 당일 올라온
동국대학교 홈페이지의 일반/학사/장학 공지를 알려주는
[dgu-notice-bot](https://github.com/JuYeong0413/dgu-notice-bot)이 2022년 3월 2일 동국대학교 홈페이지 개편과 관리자 개인 사정으로 인해 알림 서비스를 종료하게 되어, 개편된 홈페이지에 맞게 코드를 수정하고 새롭게 만든 디스코드 공지봇.  

기존과 동일하게 채널 메시지를 통해 공지를 알려주며, 사용자 채널과 명령어 등이 추가되었다.

## Environment
OS: Window 10
* Python 3.9.1
* requests
* [discord.py](https://github.com/Rapptz/discord.py)  

기타 사용된 패키지 전체는 requirement.txt를 통해 확인하실 수 있습니다.

## Running the server locally
1. Clone this repository.
```terminal
git clone https://github.com/c2lv/bampal2.git
```
2. Change directory and activate virtualenv.
```terminal
cd bampal2
pip3 install virtualenv
virtualenv "Enter Your Virtual Environment Name"
source "Enter Your Virtual Environment Name"/Scripts/activate
```
3. Add Discord bot token in `BOT_TOKEN` (Config Var).
```terminal
export BOT_TOKEN="Enter Your Discord Bot Token"
```
4. Install the requirements.
```terminal
pip3 install -r requirements.txt
```
5. Set channel ID in `const.py`
6. Run `discord_bot.py` file.
```terminal
python3 discord_bot.py
```

## Reference
[DiscordBot] 파이썬으로 디스코드 봇 만들기 -1~2  
- https://omoknooni.tistory.com/18?category=873653  
- https://omoknooni.tistory.com/19?category=873653  

디스코드 채널 아이디 알아내기
- https://neony.tistory.com/3  

사이트 정보 추출하기 - beautifulsoup 사용법 (1~2)
- https://wikidocs.net/85739
- https://wikidocs.net/86334

디스코드 봇 강좌 - 1~5편, 번외편
- https://ioxoi.tistory.com/category/%5B%EA%B0%9C%EB%B0%9C%EC%9E%90%5DDFR-%ED%8C%8C%EC%9D%B4%EC%8D%AC/%EB%94%94%EC%8A%A4%EC%BD%94%EB%93%9C%20%EB%B4%87

Send a message to a Discord channel at a certain time once a week
- https://www.reddit.com/r/Discord_Bots/comments/pc0k1k/send_a_message_to_a_discord_channel_at_a_certain/

명령어 에러처리
- https://velog.io/@chaejm55/5.-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%97%90%EB%9F%AC%EC%B2%98%EB%A6%AC

Cog
- https://velog.io/@chaejm55/13.-Cog-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B01

헤로쿠 환경변수 설정하고 파이썬에서 사용하기
- https://programming4myself.tistory.com/6

헤로쿠 무료시간 1000시간으로 늘리기
- https://programming4myself.tistory.com/7
- https://nhj12311.tistory.com/283

Heroku 로그보기
- https://dev-kiha.github.io/heroku/2021/09/23/02.html

Heroku에 로그인 된 상태에서 Terminal에 다음과 같이 입력  
> heroku logs -a [앱이름]

최근 150줄을 출력하고 싶을 때는 다음과 같이 입력 (-n 옵션이 없을 경우 최근 100줄을 출력)
> heroku logs -n 150

## Problem

- API가 반환한 값을 어떻게 확인할 수 있는지, 어떻게 해결해야 하는 지 잘 모르겠다.  
해당 에러가 발생하면 봇이 에러 메시지를 출력하도록 on_command_error() 내부에 조건문을 하나 추가했다.

```terminal
discord.errors.HTTPException: 429 Too Many Requests (error code: 0): 
You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently. 
Please read our docs at https://discord.com/developers/docs/topics/rate-limits to prevent this moving forward.
```
