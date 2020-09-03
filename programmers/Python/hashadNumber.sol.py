# list 안에 for 문 이용하여 string iterable 화
# list 내부 값 sum 으로 합침
# n 을 sum 으로 나눈 결과 값 출력

# 배울 점
# string 도 for 문으로 각 요소 출력 가능.
# return 값에 비교 연산자 사용.-

def solution(n):
    return n % sum([int(c) for c in str(n)]) == 0
