# 10871 - X보다 작은 수
# 2022-10-18


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    m = list()
    for i in A:
        if i < X:
            m.append(i)
    print(" ".join(map(str, m)))


solve()
