# sorted 함수로 정렬 값 list 로 return
# join 함수로 병합

def solution(s):
    return ''.join(sorted(s, reverse=True))
