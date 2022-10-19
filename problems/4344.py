# 4344 - 평균은 넘겠지
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    C = int(input())
    for _ in range(C):
        l = list(map(int, input().split()))
        N = l[0]
        scores = l[1:]
        avg = sum(scores) / N
        count = 0
        for score in scores:
            if score > avg:
                count += 1
        r = str()
        if r[::-1][:2] == "0.":
            r = r + "00"
        print("{:.3f}%".format(round(count / N * 100, 3)))


solve()
