# 2941 - 크로아티아 알파벳
# 2022-10-19


import sys


def input() -> str:
    return sys.stdin.readline().rstrip()


def solve():
    words = input()
    words = (
        words.replace("c=", "0")
        .replace("c-", "0")
        .replace("dz=", "0")
        .replace("d-", "0")
        .replace("lj", "0")
        .replace("nj", "0")
        .replace("s=", "0")
        .replace("z=", "0")
    )
    print(len(words))


solve()
