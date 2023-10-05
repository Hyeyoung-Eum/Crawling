from time import time
from urllib.request import Request, urlopen
import asyncio

urls= ['https://www.google.co.kr/search?q=' + i
for i in ['apple','pear','grape','pineapple','orange','strawberry']]

async def fetch(url):
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    #.run_in_executor()는, 비동기 프로그래밍에서 동기 코드를 실행하기 위해 사용된다.
    #.run_in_executor(None, 실행할 함수, (실행할 함수에 넣을 인자))
        #None : 기본 실행자(Executor)가 사용
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)

    return len(page)

async def main(): #await는 async def안에서만 가능하기 때문에, 메인 함수도 이렇게 비동기로 선언해준다
    #main에서는 네이티브 코루틴 여러 개를 동시에 실행한다.
        #따라서 asyncio.ensure_future를 사용하여 태스크 객체(asyncio.Task)를 만든다. 결과값을 모두 한 곳에 모았다가, 모두 모이면 그때 출력할 것이기 때문이다.

    #태스크(future) 객체를 리스트로 만든다
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
    #모든 퓨처 객체(=태스크 객체, 코루틴 객체)가 끝날 때까지 기다린 뒤 결과를 한꺼번에 가져온다.
    #도착한 순서에 따라 달라질 수 있기 때문에, 객체를 넣은 순서와 리스트의 요소 순서는 다를 수 있다.
    result = await asyncio.gather(*futures)
    print(result)

begin=time()
loop = asyncio.get_event_loop() #이벤트 루프를 얻음
loop.run_until_complete(main())
loop.close()
end = time()

print('실행 시간 : {0: .3f}초'.format(end-begin))