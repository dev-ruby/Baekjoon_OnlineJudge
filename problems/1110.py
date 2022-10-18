# 1110 - 더하기 사이클
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def cycle(n) -> int:
    return n % 10 * 10 + (n % 10 + n // 10) % 10


def solve():
    N = int(input())
    count = 1
    cur = cycle(N)
    while N != cur:
        count += 1
        cur = cycle(cur)

    print(count)


solve()
