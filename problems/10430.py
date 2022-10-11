# 10430 - 나머지
# 2022-10-11


def solve():
    a, b, c = map(int, input().split())
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c)


solve()
