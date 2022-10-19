# 2562 - 최댓값
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    numbers = [int(input()) for _ in range(9)]
    max_number = max(numbers)

    for i in range(9):
        if max_number == numbers[i]:
            print(max_number)
            print(i + 1)
            break


solve()
