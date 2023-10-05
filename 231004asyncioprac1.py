from time import time
from urllib.request import Request, urlopen

urls= ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]

begin = time()
result =[]

for url in urls:
    #request 객체 생성
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #UA가 없으면 403 에러 발생하는 것 방지
    #urlopen은 request 객체를 인자로 받아, 웹 서버에 HTTP 요청을 보내고 응답을 받아온다
    response = urlopen(request)
    #read()는 HTML내용을 문자열로 가져온다.
    page = response.read() 

    result.append(len(page)) #페이지 길이 읽어서 추가

print(result)
end = time()
print('실행 시간: {0:.3f}초'.format(end-begin))