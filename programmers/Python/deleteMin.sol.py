# 이터러블을 이용
# if 를 이용하여 가장 작은 수 보다 큰 수만 return

def solution(arr):
    return [i for i in arr if i > min(arr)] or [-1]
