# 1712 - 손익분기점
# 2022-10-21


import sys
import math


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    A, B, C = map(int, input().split())
    if B >= C:
        print(-1)
        return
    print(math.floor(A / (C - B)) + 1)


solve()
