# 25304 - 영수증
# 2022-10-18


def solve():
    X = int(input())
    N = int(input())
    summary = 0
    for _ in range(N):
        a, b = map(int, input().split())
        summary += a * b
    print("Yes" if summary == X else "No")


solve()
