# 방법 1 : list 안에 분리된 n 삽입
# sorted 함수로 list 정렬
# revered 함수로 뒤집음
# join 함수로 병합 및 int 로 정수화

def solution(n):

    numberList = reversed(sorted([i for i in str(n)]))
    return int("".join(numberList))


solution(90776)
