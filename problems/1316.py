# 1316 - 그룹 단어 체커
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    count = 0

    for _ in range(N):
        used_alphabet = list()
        prev_char = ""
        words = input()
        cur = 1
        for char in words:
            if char != prev_char:
                used_alphabet.append(prev_char)
            prev_char = char
            if char in used_alphabet:
                cur = 0
        count += cur

    print(count)


solve()
