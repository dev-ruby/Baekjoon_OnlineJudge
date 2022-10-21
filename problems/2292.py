# 2292 - 벌집
# 2022-10-21


import sys
import math


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    count = round(math.sqrt(((N - 1) / 3))) + 1
    print(count)


solve()
