# 10951 - A+B - 4
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    while True:
        try:
            print(sum(map(int, input().split())))
        except EOFError:
            break


solve()
