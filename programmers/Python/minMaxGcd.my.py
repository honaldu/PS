# math 모듈을 이용해 최소 공배수 return
# 유클리드 호제법을 이용해 n,m 을 곱한 수에 최소 공배수를 나누어서 return
from math import gcd


def solution(n, m):
    return [gcd(n, m), (n*m)//gcd(n, m)]
