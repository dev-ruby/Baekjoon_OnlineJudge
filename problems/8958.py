# 8958 - OX퀴즈
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    T = int(input())
    for _ in range(T):
        res = input()
        score = 0
        cur = 0
        for r in res:
            if r == "O":
                cur += 1
            else:
                cur = 0
            score += cur
        print(score)


solve()
