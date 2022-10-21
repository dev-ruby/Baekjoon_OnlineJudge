# 5622 - 다이얼
# 2022-10-21


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    S = input().lower()
    count = 0
    for char in S:
        if char in "abc":
            count += 3
        elif char in "def":
            count += 4
        elif char in "ghi":
            count += 5
        elif char in "jkl":
            count += 6
        elif char in "mno":
            count += 7
        elif char in "pqrs":
            count += 8
        elif char in "tuv":
            count += 9
        elif char in "wxyz":
            count += 10
    print(count)


solve()
