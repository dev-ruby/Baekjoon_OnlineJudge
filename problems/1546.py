# 1546 - 평균
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    scores = list(map(int, input().split()))
    new_scores = list()
    M = max(scores)
    for score in scores:
        new_scores.append(score / M * 100)
    print(sum(new_scores) / N)


solve()
