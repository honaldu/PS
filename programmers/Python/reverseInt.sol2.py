# str 된 함수 이터러블로 list 에 담음
# [::-1] 로 뒤집음

def solution(n):
    return [int(i) for i in str(n)][::-1]
