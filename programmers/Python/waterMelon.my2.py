# n 값을 2로 나눈 몫과 나머지 이용해 이터러블 생성
# string index 이용해 n에 따른 마지막 글자 커팅

def solution(n):
    return "".join(["수박" for i in range(n//2+n % 2)])[:n]
