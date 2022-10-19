# 1157 - 단어 공부
# 2022-10-19


from itertools import count
import sys
from collections import defaultdict


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    count_dict = defaultdict(int)
    words = input().lower()
    for char in words:
        count_dict[char] += 1
    count_list = sorted(list(count_dict.items()), key=lambda x: x[1], reverse=True)
    if len(count_list) >= 2:
        if count_list[0][1] == count_list[1][1]:
            print("?")
            return
    print(count_list[0][0].upper())


solve()
