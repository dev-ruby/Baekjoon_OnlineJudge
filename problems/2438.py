# 2438 - 별 찍기 - 1
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    for i in range(N):
        print("*" * (i + 1))


solve()
