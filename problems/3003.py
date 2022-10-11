# 3003 - 킹, 퀸, 룩, 비숍, 나이트, 폰
# 2022-10-11


def solve():
    pieces = list(map(int, input().split()))
    print(
        1 - pieces[0],
        1 - pieces[1],
        2 - pieces[2],
        2 - pieces[3],
        2 - pieces[4],
        8 - pieces[5],
    )


solve()
