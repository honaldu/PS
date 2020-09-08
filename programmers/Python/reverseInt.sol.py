# 함수형 프로그래밍

# reversed 된 n 을 map 함수로 int 적용
# list 로 map 된 n 담음

def solution(n):
    return list(map(int, reversed(str(n))))
