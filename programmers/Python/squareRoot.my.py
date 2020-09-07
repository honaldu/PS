#
import math


def solution(n):
    num = math.sqrt(n)

    return pow(num+1, 2) if num == int(num) else -1
