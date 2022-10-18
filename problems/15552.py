# 15552 - 빠른 A+B
# 2022-10-18

import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    T = int(input())
    for _ in range(T):
        print(sum(list(map(int, input().split()))))


solve()
