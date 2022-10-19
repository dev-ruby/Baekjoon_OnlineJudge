# 4673 - 셀프 넘버
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def d(n: int) -> int:
    return n + sum(map(int, list(str(n))))


def solve():
    is_self_number = [True for _ in range(10000)]
    is_self_number[0] = False
    self_number = []
    cur = 1
    for i in range(1, 10001):
        cur = d(i)
        while cur < 10000:
            is_self_number[cur] = False
            cur = d(cur)
    for i in range(10000):
        if is_self_number[i]:
            self_number.append(i)

    print(" ".join(map(str, self_number)))


solve()
