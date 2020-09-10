# iterable 이용위해 n string 화
# 요소에 int 함수로 숫자화
# sum 함수로 list 합

def solution(n):
    return sum([int(i) for i in str(n)])


solution(257)
