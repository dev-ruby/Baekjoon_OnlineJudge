# 1330 - 두 수 비교하기
# 2022-10-17


def solve():
    A, B = map(int, input().split())
    if A > B:
        print(">")
    elif A == B:
        print("==")
    else:
        print("<")


solve()
