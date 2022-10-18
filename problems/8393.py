# 8393 - 합
# 2022-10-18


def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    avg = (1 + n) / 2
    print(int(avg * n))


solve()
