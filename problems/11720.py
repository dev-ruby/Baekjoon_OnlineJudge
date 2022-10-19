# 11720 - 숫자의 합
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    _ = input()
    print(sum(map(int, list(str(input())))))


solve()
