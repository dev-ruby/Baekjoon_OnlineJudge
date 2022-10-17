# 14681 - 사분면 고르기
# 2022-10-17


def solve():
    x, y = map(int, (input(), input()))
    if x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    else:
        if y > 0:
            print(2)
        else:
            print(3)


solve()
