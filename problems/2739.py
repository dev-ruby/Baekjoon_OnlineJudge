# 2739 - 구구단
# 2022-10-17


def solve():
    n = int(input())
    for i in range(9):
        print(f"{n} * {i+1} = {n*i+n}")


solve()
