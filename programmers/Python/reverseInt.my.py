# n 을 string 화
# reversed 함수로 n reverse
# 이터러블 사용하기 위해 list 함수 사용
# 이터러블에 int 함수로 숫자화

def solution(n):
    return [int(i) for i in list(reversed(str(n)))]
