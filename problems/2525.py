# 2525 - 오븐 시계
# 2022-10-17


def solve():
    H, M = map(int, input().split())
    T = int(input())
    mins = H * 60 + M
    clock_time = (mins + T) % 1440
    hour, minute = divmod(clock_time, 60)
    print(hour, minute)


solve()
