# 10818 - 최소, 최대
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    numbers = list(map(int, input().split()))
    print(min(numbers), max(numbers))


solve()
