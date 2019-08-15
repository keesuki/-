# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법
# urlopen은 수신된 데이터를 매개변수로 담을 수 있다.urlretrieve와는 그부분이 차이다.

import urllib.request as req
from urllib.error import URLError, HTTPError  # 주소 오타 해결
import os

# 다운로드 경로 및 파일명
path_list = ["./example/test1.jpg","./example/index.html" ]

# 다운로드 리소스 URL
target_url = ["http://blogfiles.naver.net/20121010_218/rladmsalxla_1349861389877r3uYU_JPEG/2012-10-10_18%3B26%3B13.jpg", "http://google.com"]

for i, url in enumerate(target_url):
    # 예외처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("==============================================")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print("==============================================")
        
        with open(path_list[i], "wb") as c:  #wb는 바이너리 파일저장
            c.write(contents)


    except HTTPError as e:
        print("Download failed")
        print("HTTPError code : ", e.code)
    except URLError as e:
        print("Download failed")
        print("URL Error Reason : ", e.reason)
    
    #성공
    else:
        print()
        print("Download Succeed")


