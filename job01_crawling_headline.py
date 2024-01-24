import pandas as pd
from bs4 import BeautifulSoup #pip install bs4
import requests # HTTP 요청을 보내기 위한 requests 라이브러리
import re # 파이썬 기본 패키징
import pandas # 데이터 조작 및 분석을 위한 Pandas
import datetime # 날짜 및 시간 다루기 위한 datetime 모듈

# 뉴스 카테고리 정의
category = ['politics','Economic','social','Culture','World','IT']
# 스크래핑할 뉴스 웹사이트의 URL
# url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100' # 10인 건가??
# # URL로 HTTP GET 요청 보내기
# headers = {"User - Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}


# resp = requests.get(url,headers = headers)
#
# print(resp)
# print(type(resp))
# print(list(resp))
#
# # 웹서버는 웹페이지를 요청하고 응답하는 것.
# # 256 씩 4개 ...?
# # 서버 : 요청을 기다리는 애.
# # 클라이언트: 요청을 하는 애.
# # 서버 만들 때는 리눅스로 만들음.
# # resquest를 하면
#
# # 웹페이지의 HTML 내용을 파싱하기 위한 BeautifulSoup 객체 생성
# soup = BeautifulSoup(resp.text,'html.parser')
# print(soup) # soup 으로 바꾸니까
#
# # 'sh_text_headline' 클래스를 가진 모든 요소 선택
# title_tags = soup.select('.sh_text_headline')
# print(title_tags) # 선택된 태그들을 출력하여 확인 할 수 있다.
# print(len(title_tags)) # 선택된 태그들의 개수를 출력합니다.
# print(type(title_tags[0])) # 선택된 태그 중 첫 번째 태그의 데이터 타입을 출력합니다.
#
# # 선택된 태그에서 제목 추출, 한글 및 알파벳 이외의 문자 제거
# titles = []
# for title_tag in title_tags:
#     titles.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ',title_tag.text)) # 가부터 힣까지, a부터 z 까지, A-Z 까지를 빼고 나머지를 빈칸으로 채워라.
# print(titles)

df_titles = pd.DataFrame()
re_title = re.compile('[^가-힣|a-z|A-Z]')
headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

for i in range(6):
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.sh_text_headline')
    titles = []
    for title_tag in title_tags:
        titles.append(re.compile('[^가-힣|a-z|A-Z]').sub('', title_tag.text))
    df_section_titles = pd.DataFrame(titles, columns = ['titles'])  #titles가지고 데이터프레임만듬
    df_section_titles['category'] = category[i] #카테고리라는 항목을 추가함.
    df_titles = pd.concat([df_titles,df_section_titles], axis='rows', ignore_index=True)

print(df_titles.head())
df_titles.info()
print(df_titles['category'].value_counts())
df_titles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d')),index=False)




