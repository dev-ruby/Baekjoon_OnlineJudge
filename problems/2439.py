# 2439 - 별 찍기 - 2
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    for i in range(N):
        print(" " * (N - i - 1) + "*" * (i + 1))


solve()
