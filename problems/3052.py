# 3052 - 나머지
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    numbers = set(map(lambda x: x % 42, [int(input()) for _ in range(10)]))
    print(len(numbers))


solve()
