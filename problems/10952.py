# 10952 - A+B - 5
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    while True:
        s = sum(map(int, input().split()))
        if s == 0:
            break
        print(s)


solve()
