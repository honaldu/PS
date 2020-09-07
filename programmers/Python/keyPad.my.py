# 이터러블로 numbers 순회
# left, right 기본값 설정
# if 분기점을 키패드로 나눔
# middle 의 if 분기점을 손잡이로 나눔.

def solution(numbers, hand):
    left = "*"
    right = "#"
    leftKey = ["1", "4", "7", "*"]
    middleKey = ["2", "5", "8", "0"]
    rightKey = ["3", "6", "9", "#"]
    answer = ""
    for i in numbers:
        if leftKey.index(i) == True:
            answer.add("L")
            left = i
        if rightKey.index(i) == True:
            answer.add("R")
            right = i
        else:
            print(i)
