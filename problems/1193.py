# 1193 - 분수찾기
# 2022-10-21


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    line = 1
    while N > line:
        N -= line
        line += 1
    if line % 2 == 0:
        print(f"{N}/{line-N+1}")
    else:
        print(f"{line-N+1}/{N}")


solve()
