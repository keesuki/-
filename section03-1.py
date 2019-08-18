# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)

# 사이트요청 정보확인
    # 엔카 사이트 정보 수신
    # Get 파라미터 요청
    # 수신 데이터 디코딩(Decoding)
    # 요청 URL 정보 분석


import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러정보 출력
print("1. type : {}".format(type(mem)))
print("2. geturl : {}".format(mem.geturl()))  # 가져온 url주소
print("3. status : {}".format(mem.status))  # 상태보기
print("4. headers : {}".format(mem.getheaders())) # 헤더 정보 보기
print("5. getcode : {}".format(mem.getcode())) # 코드 상태보기
print("6. read : {}".format(mem.read(100).decode('utf-8')))  #기존에는 eucrk형태, 소스 가져오기
print("7. parse : {}".format(urlparse('http://www.encar.co.kr?id=test&pw=1111')))  # 분리해서 보여주는 아주 중요한 함수 ★, get방식

# 기본 요청2(ipify)
API = "https://api.ipify.org"

# Get 방식 Parameter
values = {
    'format': 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)  # get 방식 형태로 변경해줌 dict -> get형태
print('after param : {}'.format(params))  

# 요청 url 생성
URL = API + "?" + params
print("요청 URL = {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()


# 수신 데이터 디코딩
text = data.decode('UTF-8')
print('response : {}'.format(text))
