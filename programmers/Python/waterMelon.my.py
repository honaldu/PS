# n 을 2로 나눈 몫만큼 수박 출력
# 나머지 값에 따라 수 더함

def solution(n):
    string = ""
    for i in range(n//2):
        string += "수박"
    if (n % 2 == 1):
        string += "수"
    return string
