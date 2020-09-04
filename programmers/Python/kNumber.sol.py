# 함수형 프로그래밍
# list 함수로 list 화
# map 함수로 commands 활용
# lambda 로 commands 인자 선언


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
