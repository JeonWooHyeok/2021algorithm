import datetime
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')
print()
print('지금은 ' + nowDate)

print('공항 날씨 한 눈에 보기')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%B8%EC%B2%9C%EA%B3%B5%ED%95%AD+%EB%82%A0%EC%94%A8&oquery=%EA%B9%80%ED%95%B4+%EA%B3%B5%ED%95%AD+%EB%82%A0%EC%94%A8&tqi=hh3olsp0JywssOWSlVosssssshw-177471')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('span', "num")
cast = soup.find('p', "summary")
print('-> 인천 공항 날씨 :', temps.get_text(),cast.get_text())

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EA%B9%80%ED%8F%AC+%EA%B3%B5%ED%95%AD+%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('span', "num")
cast = soup.find('p', "summary")
print('-> 김포 공항 날씨 :', temps.get_text(),cast.get_text())

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EA%B0%95%EC%84%9C%EA%B5%AC+%EB%8C%80%EC%A0%80+2%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EA%B9%80%ED%95%B4+%EA%B3%B5%ED%95%AD&tqi=hh3qTdprvTVssbsHERdssssstC8-281956')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('span', "num")
cast = soup.find('p', "summary")
print('-> 김해 공항 날씨 :', temps.get_text(),cast.get_text())
print()

qus = input("어디 공항으로 가시나요?\n1.인천공항\n2.김포공항\n3.김해공항\n")
if qus == '인천공항':
    print('인천공항 확인하였습니다.')
    req = input('표는 예매 하셨습니까? 네/아니요')
    if req == '네':
        print('좋은 여행 되십시요 :)')
    elif req == '아니요':
        tic = input('인천공항에서 출발하는 항공편을 보여드릴까요? 네/아니요')
        if tic == '네':
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://www.airport.kr/ap/ko/dep/depPasSchList.do'
            browser.get(url)
            time.sleep(1000)
        else:
            print('서비스를 이용해주셔서 감사합니다 :)')
    else:
        print('네 혹은 아니요로 대답 해주세요.')
elif qus == '김포공항':
    print('김포공항 확인하였습니다.')
    req = input('표는 예매 하셨습니까? 네/아니요')
    if req == '네':
        print('좋은 여행 되십시요 :)')
    elif req == '아니요':
        tic = input('김포공항에서 출발하는 항공편을 보여드릴까요? 네/아니요')
        if tic == '네':
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://www.airport.co.kr/gimpo/cms/frCon/index.do?MENU_ID=1010'
            browser.get(url)
            time.sleep(1000)
        else:
            print('서비스를 이용해주셔서 감사합니다 :)')
    else:
        print('네 혹은 아니요로 대답 해주세요.')
elif qus == '김해공항':
    print('김해공항 확인하였습니다.')
    req = input('표는 예매 하셨습니까? 네/아니요')
    if req == '네':
        print('좋은 여행 되십시요 :)')
    elif req == '아니요':
        tic = input('김해공항에서 출발하는 항공편을 보여드릴까요? 네/아니요')
        if tic == '네':
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://www.airport.co.kr/gimhae/index.do#slide3'
            browser.get(url)
            time.sleep(1000)
        else:
            print('서비스를 이용해주셔서 감사합니다 :)')
    else:
        print('네 혹은 아니요로 대답 해주세요.')
else:
    print('위의 세 공항 외 다른 공항은 서비스를 지원하지 않습니다. 죄송합니다 :(')