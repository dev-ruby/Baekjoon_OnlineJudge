# 9498 - 시험 성적
# 2022-10-17


def solve():
    score = int(input()) // 10
    grade = {10: "A", 9: "A", 8: "B", 7: "C", 6: "D"}.get(score)
    if grade is None:
        grade = "F"

    print(grade)


solve()
