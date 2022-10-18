# 11022 - A+B - 8
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print(f"Case #{i+1}: {a} + {b} = {a+b}")


solve()
