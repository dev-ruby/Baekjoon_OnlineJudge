# 1065 - 한수
# 2022-10-19


import sys

number_sorted = "0123456789"
number_sorted_reverse = "9876543210"


def input() -> str:
    return sys.stdin.readline().rstrip()


def is_hansu(n: int) -> bool:
    if n < 100:
        return True
    elif n == 1000:
        return False
    else:
        gap = n // 10 % 10 - n % 10
        return n // 100 % 10 - gap == n // 10 % 10


def solve():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1

    print(count)


solve()
