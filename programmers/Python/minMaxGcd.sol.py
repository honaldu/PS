# 유클리드 호제법을 이용해 최대 공약수를 구함
# 유클리드 호제법을 이용해 a*b 를 최대 공약수로 나누어 최소 공배수 구함.

def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return [c, int(a*b/c)]
