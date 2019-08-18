# Section03-2
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(2) - RSS가져오기
# RSS란? 사이트를 직접 방문하지 않고도 새로운글, 소식등을 제공해주는 일종의 사이트에서 보내주는 소식지

import urllib.request
import urllib.parse

# 행정안전부 : https://www.mois.go.kr
# 행정안전부 RSS API URL
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간확인
# print(params)

# 연속해서 4회 요청
for c in params:
    # 파라미터 출력
    param=urllib.parse.urlencode(c)
    # print(param)

    # url 완성
    url = API + "?" + param
    # url 출력
    print("url: ", url)

    # 요청
    res_data = urllib.request.urlopen(url).read()
    # print(res_data)

    # 수신 후 디코딩
    contents = res_data.decode("UTF-8")
    print("*" * 150)
    print("*" * 150)
    print("*" * 150)
    print("*" * 150)
    print(contents)