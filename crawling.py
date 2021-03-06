import requests, re, time, const
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

def get_list_3(url):
    title, link = list(), list()
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        i = 0
        while True:
            _title = soup.select_one(f'#s_right > div:nth-child(2) > table > tr > td > form > table > tr:nth-child({2*i+1}) > td:nth-child(2) > a')
            if _title == None:
                break
            _title = _title.text
            _link = soup.select_one(f'#s_right > div:nth-child(2) > table > tr > td > form > table > tr:nth-child({2*i+1}) > td:nth-child(2) > a').get('href')
            _link = url[:23] + _link[2:]
            date = soup.select_one(f'#s_right > div:nth-child(2) > table > tr > td > form > table > tr:nth-child({2*i+1}) > td:nth-child(5) > span').text.strip()
            mark = soup.select_one(f'#s_right > div:nth-child(2) > table > tr > td > form > table > tr:nth-child({2*i+1})').get('bgcolor') # 공지는 F5F5F5
            if (today == date) and (mark != "F5F5F5"):
                title.append(_title)
                link.append(_link)
            i += 1
    else:
        print(response.status_code)

    return title, link

def get_list_2(url):
    title, link = list(), list()
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        for i in range(1, 31):
            _title = soup.select_one(f'#fboardlist > div > table > tbody > tr:nth-child({i}) > td.td_subject > div > a').text.strip()
            _link = soup.select_one(f'#fboardlist > div > table > tbody > tr:nth-child({i}) > td.td_subject > div > a').get('href')
            date = soup.select_one(f'#fboardlist > div > table > tbody > tr:nth-child({i}) > td.td_datetime').text
            if today == date:
                title.append(_title)
                link.append(_link)
    else:
        print(response.status_code)

    return title, link

def get_list_1(url):
    title, link = list(), list()
    response = requests.get(url)
    if response.status_code == 200: # 응답코드 200(성공, 서버가 요청을 제대로 처리했다는 뜻)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        today = re.sub(r'[^0-9]', '', today) # 숫자 이외의 문자 제거
        detail_url = url[:-4] + "detail/"
        for i in range(1, 17):
            _title = soup.select_one(f'#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child({i}) > a > div.top > p')
            _link = soup.select_one(f'#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child({i}) > a').get('onclick')
            _link = re.findall('\(([^)]+)', _link) # goDetail 함수 괄호 안 인자 추출
            date = soup.select_one(f'#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child({i}) > a > div.top > div.info > span:nth-child(1)').text.strip()
            date = re.sub(r'[^0-9]', '', date) # 숫자 이외의 문자 제거
            mark = soup.select_one(f'#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child({i}) > a > div.mark > span').get('class')
            if (today == date) and (mark[0] == "num"): # 오늘 날짜의 공지이고 고정 공지가 아니라면
                title.append(_title.text.strip())
                link.append(detail_url + _link[0])
    else:
        print(response.status_code)

    return title, link

def run(url, notice_type):
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y년 %m월 %d일')
    if notice_type in const.TYPE1:
        titles, urls = get_list_1(url)
    elif notice_type in const.TYPE2:
        titles, urls = get_list_2(url)
    elif notice_type in const.TYPE3:
        titles, urls = get_list_3(url)
    length = len(titles)
    str = ""
    if (length > 0):
        str = f":bulb: {today} {notice_type}공지입니다.\n"
        for i in range(len(titles)):
            str = f"{str}\n{titles[i]}\n{urls[i]}\n"
    else:
        str = f":bulb: {today} {notice_type}공지는 없습니다."

    return str