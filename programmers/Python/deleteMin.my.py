# if 함수로 arr 의 길이에 따라 분기.
# arr 의 min 값 remove 로 제거

def solution(arr):
    if (len(arr) == 1):
        return [-1]
    arr.remove(min(arr))
    return arr
