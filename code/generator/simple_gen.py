from typing import List


def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)
    return numbers


def fib1():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


for n in fib1():
    if n > 1000:
        break
    print(n, end=',')
