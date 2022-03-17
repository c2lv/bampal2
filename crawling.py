import requests, re, time
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

def get_list(url):
    title, link = list(), list()
    response = requests.get(url)
    if response.status_code == 200: # 응답코드 200(성공, 서버가 요청을 제대로 처리했다는 뜻)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        detail_url = url[:-4] + "detail/"
        for i in range(1, 17):
            _title = soup.select_one('#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child(' + str(i) + ') > a > div.top > p')
            _link = soup.select_one('#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child(' + str(i) + ') > a').get('onclick')
            _link = re.findall('\(([^)]+)', _link) # goDetail 함수 괄호 안 인자 추출
            date = soup.select_one('#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child(' + str(i) + ') > a > div.top > div.info > span:nth-child(1)')
            mark = soup.select_one('#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child('+ str(i) + ') > a > div.mark > span').get('class')
            if (today == date.text.strip()) and (mark[0] == "num"): # 오늘 날짜의 공지이고 고정 공지가 아니라면
                title.append(_title.text.strip())
                link.append(detail_url + _link[0])
    else:
        print(response.status_code)

    return title, link

def run(url, notice_type):
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y년 %m월 %d일')
    titles, urls = get_list(url)
    length = len(titles)
    str = ""
    if (length > 0):
        str = ":bulb: {} {}공지입니다.\n".format(today, notice_type)
        for i in range(len(titles)):
            str = "{}\n{}\n{}\n".format(str, titles[i], urls[i])
    else:
        str = ":bulb: {} {}공지는 없습니다.".format(today, notice_type)

    return str