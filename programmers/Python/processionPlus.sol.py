# zip 첫번째로 arr1, arr2 의 같은 index를 묶은 후 묶인 zip을 다시 zip으로 묶어 같은 index 끼리 하나의 배열 안에 넣음
# 각 요소를 더해서 return
def solution(arr1, arr2):
    procession = [[c+d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return procession
