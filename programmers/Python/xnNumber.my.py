# 반복문의 i 의 증가값을 이용함.

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i*x)
    return answer
