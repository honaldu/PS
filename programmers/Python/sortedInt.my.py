# 방법 1 : list 안에 분리된 n 삽입
# sorted 함수로 list 정렬
# 병합된 list return


def solution(n):
    numberList = sorted(list(map(int, (str(n)))))
    return numberList
