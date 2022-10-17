# 2884 - 알람 시계
# 2022-10-17


def solve():
    H, M = map(int, input().split())
    mins = H * 60 + M
    clock_time = mins - 45 if mins >= 45 else 1440 + mins - 45
    hour, minute = divmod(clock_time, 60)
    print(hour, minute)


solve()
