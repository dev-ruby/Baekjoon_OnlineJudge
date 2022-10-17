# 2480 - 주사위 세개
# 2022-10-17


def solve():
    a, b, c = map(int, input().split())
    count = len(set((a, b, c)))
    if count == 1:
        print(10000 + 1000 * a)
    elif count == 2:
        if a == b:
            print(1000 + 100 * a)
        elif b == c:
            print(1000 + 100 * b)
        else:
            print(1000 + 100 * c)
    else:
        print(100 * max((a, b, c)))


solve()
