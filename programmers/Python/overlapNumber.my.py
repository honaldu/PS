# number 변수를 둬서 이전 수와 비교
# 배열 하나 추가
# 이터러블로 number 값과 i 값이 같지 않으면 새로운 배열에 추가.
# number 값 i로 변경해 매번 비교.

def solution(arr):
    number = None
    arr2 = []
    for i in arr:
        if i != number:
            arr2.append(i)
        number = i
    return arr2


print(solution([1, 1, 3, 3, 0, 1, 1]))
