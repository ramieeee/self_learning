import requests
import time
import sys
from bs4 import BeautifulSoup
import atexit

TARGET_URL = 'https://notify-api.line.me/api/notify'
TOKEN = '9ySbbZxGDt33gWGefpBaX4oQfCZrAbtvQLq8GndcgNz'

# 문화재청 url
url1 = 'https://www.cha.go.kr/multiBbz/selectMultiBbzList.do?bbzId=newexam&mn=NS_01_06'
# 국립문화재연구소 url
url2 = 'https://www.nrich.go.kr/kor/boardList.do?menuIdx=285&bbscd=40'
# 경기문화재연구원 url
url3 = 'https://gjicp.ggcf.kr/archives/category/notice'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

# 1. 라인 API 키 발금
# 2. 본인 윈도우 계정 이름 넣기(path_dir에)

def send_Line(text):
    try:
        response = requests.post(
            TARGET_URL,
            headers={
                'Authorization': 'Bearer ' + TOKEN
            },
            data={
                'message': text
            }
        )
    except:
        sys.exit()

def check_text(fileName, text):
    with open(fileName, 'r') as f:
        temp = f.readline()
        if temp == text:
            return True
        return False

def write_over(fileName, text):
    with open(fileName, 'w') as f:
        f.write(text)

def one(url):
    # 문화재청 새 글 추출
    file_name = 'one.data'
    html1 = requests.get(url, headers=header, timeout=5.0).text
    soup = BeautifulSoup(html1, "html.parser")
    findAll1 = soup.find_all('td')
    temp = str(findAll1[0])
    num1 = ''
    for i in temp:
        if i >= '0' and i <= '9':
                num1 += i
    try:
        if check_text(file_name, num1) == False:
            write_over(file_name, num1)
            send_Line('문화재청 웹페이지에 새 개시글이 등록되었습니다. 데헷뿌잉뀨 ^ -^/')
    except FileNotFoundError:
        write_over(file_name, num1)
        send_Line('문화재청 데이터를 새로 등록합니다. \n폴더 내 .data 파일은 건들지 말아주세요. 데헷뿌잉뀨 ^ -^/')

def two(url):
    # 국립문화재연구소 새 글 추출
    file_name = 'two.data'
    html2 = requests.get(url, headers=header, timeout=5.0).text
    soup = BeautifulSoup(html2, "html.parser")
    findAll2 = soup.find_all('td')
    temp = str(findAll2[0])
    num2 = ''
    for i in temp:
        if i >= '0' and i <= '9':
            num2 += i
    try:
        if check_text(file_name, num2) == False:
            write_over(file_name, num2)
            send_Line('국립문화재연구소 웹페이지에 새 개시글이 등록되었습니다. 데헷뿌잉뀨 ^ -^/')
    except FileNotFoundError:
        write_over(file_name, num2)
        send_Line('국립문화재연구소 데이터를 새로 등록합니다. \n폴더 내 .data 파일은 건들지 말아주세요. 데헷뿌잉뀨 ^ -^/')

def three(url):
    # 경기문화재연구원 새 글 추출
    file_name = 'three.data'
    html3 = requests.get(url, headers=header, timeout=5.0).text
    soup = BeautifulSoup(html3, "html.parser")
    data = soup.find_all('td', {'class': 'title'})

    temp = str(data[1])
    num3 = ''
    for i in temp:
        if i >= '0' and i <= '9':
            num3 += i
    try:
        if check_text(file_name, num3) == False:
            write_over(file_name, num3)
            send_Line('경기문화재연구원 웹페이지에 새 개시글이 등록되었습니다. 데헷뿌잉뀨 ^ -^/')
    except FileNotFoundError:
        write_over(file_name, num3)
        send_Line('경기문화재연구원 데이터를 새로 등록합니다. \n폴더 내 .data 파일은 건들지 말아주세요. 데헷뿌잉뀨 ^ -^/')

send_Line('프로그램 시작\n버그나 에러는 ramieeee에게 문의하세요\n\ngithub: https://github.com/ramieeee/')

def main():
    try:
        while True:
            one(url1)
            time.sleep(0.2)
            two(url2)
            time.sleep(0.2)
            three(url3)
            time.sleep(2)
    except:
        send_Line('프로그램 강제 종료')

if __name__ == "__main__":
    main()
    send_Line('또 만나요. 쀼쮸쀼쮸')
