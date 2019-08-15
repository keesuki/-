# Section02-4
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2) _ Xpath 활용
# 세션활용 - ex>로그인을 한상태를 유지 -> 셀레늄에서 세션정보도 활용하고 고급기술 배울예정


from lxml.html import fromstring, tostring  # 전자는 웹문자를 string전환, tostring은 이쁘게 내보냄
import requests


def main():

    """
    네이버 메인 뉴스 스탠드 스크래핑 메인함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크래핑 대상 URL
    response = session.get("https://www.naver.com")  #get으로 바로 가져오기 가능 get, post 방식이 있음.(?)

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)  # urllib의 urlopen을 활용하여 똑같이 작성가능하다.

    # 딕셔너리확인
    # print(urls)


    # 결과 출력
    for name, url in urls.items():
        print(name, url)
        # 파일쓰기 가능
        # 생략

def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    # print(response.content) # 콘텐츠 확인
    root = fromstring(response.content)
    # print(root)

    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        
        # a 구조 확인
        # print(a)

        # a의 문자열 출력
        # print(tostring(a, pretty_print=True))

        name, url = extract_contents(a)
        # 딕셔너리 삽입
        urls[name] = url
    return urls

def extract_contents(dom):
    # 링크 주소
    link = dom.get("href")

    # 신문사명
    name = dom.xpath('./img')[0].get('alt')
    
    return name, link



# 스크래핑 시작
if __name__ == "__main__":
    main()