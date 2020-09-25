# 새로운 배열에 arr 값 추가
# 새로운 배열의 마지막 값 슬라이싱과  [i] 같을 시 continue 로

# index 내부 콜론시 slicing 된 list return
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a
