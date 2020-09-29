# 익스프레션 으로 조건에 맞는 배열 생성
# 배열 값에 따른 return 값 생성

def solution(arr, divisor):
    arr2 = [i for i in arr if i % divisor == 0]
    return arr2 == [] and [-1] or sorted(arr2)
