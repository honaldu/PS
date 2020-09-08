# n의 제곱근을 담은 변수 생성
# 삼항 연산자를 이용해 변수의 값과 int 처리한 변수의 값을 비교

import math


def solution(n):
    num = math.sqrt(n)
    return pow(num+1, 2) if num == int(num) else -1
