# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑


import urllib.request as req

# 파일 URL
img_url = 'http://newsimg.hankookilbo.com/2018/08/21/201808211199763759_1.jpg'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = "C:/FastCam/scrapping/example/test1.jpg"
save_path2 = "C:/FastCam/scrapping/example/index.html"

# 예외처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)   # 다운로드받을 파일과 수신정보를 받아옴
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print("------------------------")
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))


    # 성공
    print("Download Succeed")


# 안에서 정보를 찾는것을 파싱이라고 한다.