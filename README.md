# 밤팔이
  
:elephant: [채널 입장하기](https://discord.gg/6BVxgEvCM7)

평일 오후 6시마다 당일 올라온
동국대학교 홈페이지의 일반/학사/장학 공지를 알려주는
[dgu-notice-bot](https://github.com/JuYeong0413/dgu-notice-bot)이 2022년 3월 2일 동국대학교 홈페이지 개편과 관리자 개인 사정으로 인해 알림 서비스를 종료하게 되어, 개편된 홈페이지에 맞게 코드를 수정하고 새롭게 만든 디스코드 공지봇.  

기존과 동일하게 채널 메시지를 통해 공지를 알려주며, 사용자 채널과 명령어가 추가되었다.

## Environment
* Python 3.9.1
* beautifulsoup4
* requests
* [discord.py](https://github.com/Rapptz/discord.py)  

기타 사용된 패키지 전체는 requirement.txt를 통해 확인하실 수 있습니다.

## Running the server locally
1. Clone this repository.
```terminal
$ git clone https://github.com/c2lv/bampal2.git
```
2. Add Discord bot token in `secrets.json`.
```json
{
    "token": "Enter Your Discord Bot Token"
}
```
3. Install the requirements.
```terminal
$ pip3 install -r requirements.txt
```
4. Install `discord.py`
```terminal
$ python3 -m pip install -U discord.py
```
5. Set channel ID in `discord_bot.py`
6. Run `discord_bot.py` file.
```terminal
$ python3 discord_bot.py
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