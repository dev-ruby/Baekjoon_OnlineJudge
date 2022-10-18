# 11021 - A+B - 7
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    T = int(input())
    for i in range(T):
        print(f"Case #{i+1}: {sum(list(map(int, input().split())))}")


solve()
