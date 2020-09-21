# 구글링 실력 부족
# isdigit 함수로 string type 판별
# 튜플 타입 선언 및 안에 있는 값 일 시 True return 값 이용.
# isdigit 대신 isdecimal 이 적합

def solution(s):
    return s.isdecimal() and len(s) in (4, 6)
