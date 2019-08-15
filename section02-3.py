# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(1)
# lxml는 parsing tool - parsing은 html, xml부분 중 필요한 부분만 가져오는 작업임
# naver.com 의 뉴스스텐드 가져오기 and CSS의 선택자 활용
# pip install lxml, requests, cssselect


import lxml.html
import requests


def main():

    """
    네이버 메인 뉴스 스탠드 스크래핑 메인함수
    """
    # 스크래핑 대상 URL
    response = requests.get("https://www.naver.com")  #get으로 바로 가져오기 가능 get, post 방식이 있음.(?)

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)  # urllib의 urlopen을 활용하여 똑같이 작성가능하다.

    # 결과 출력
    for url in urls:
        print(url)
        # 파일쓰기 가능
        # 생략

def scrape_news_list_page(response):
    # URS 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    # print(response.content) # 콘텐츠 확인
    root = lxml.html.fromstring(response.content)
    # print(root)

    for a in root.cssselect('.api_list .api_item a.api_link'):  # class를 기준으로 순회
        # 링크
        url = a.get('href')
        urls.append(url)
    return urls

    # 신문사 명 가져오기
    # for a in root.cssselect('.api_list .api_item a.api_link .api_logo'):  # class를 기준으로 순회
    #     # 링크
    #     url = a.get('alt')
    #     urls.append(url)
    # return urls



# 스크래핑 시작
if __name__ == "__main__":
    main()