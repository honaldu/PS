# 삼항연산자와 math.sqrt 함수로 n 의 재곱근 판별
# 판별값에 따라 return
import math


def solution(n):
    typi = type(math.sqrt(n))
    return typi
