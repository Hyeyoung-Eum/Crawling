import asyncio
from time import time
class AsyncAdd:
    def __init__(self,a, b):
        self.a=a
        self.b=b

    #__aenter__에서 값을 반환하면, as에 지정한 변수에 들어감
    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self.a + self.b
    
    async def __aexit__(self, exc_type, exc_value, traceback):
            #async with as를 완전히 벗어나면 호출된다.
            #하지만 메서드 자체가 없으면 에러가 발생하니, 반드시 추가해줘야한다.
            pass

async def main():
    async with AsyncAdd(1, 2) as result:
        print(result)

start=time()
loop = asyncio.get_event_loop()

loop.run_until_complete(main())
loop.close()
end=time()
print(f'소요 시간 :{end-start}')