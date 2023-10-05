def sum_coroutine():
    total=0
    while True:
        x = (yield total) #코루틴 바깥에서 값을 받아오면서, total 값을 바깥으로 값을 전달
        total += x

co = sum_coroutine()
print(next(co))

print(co.send(1))
print(co.send(2))
print(co.send(3))