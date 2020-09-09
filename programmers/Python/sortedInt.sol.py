# string 을 바로 list 화 시킴
# sort 함수에 reverse 인자 넣어 뒤집음
# join 함수로 병합

def solution(n):
    numberList = list(str(n))
    numberList.sort(reverse=True)
    return int("".join(numberList))
