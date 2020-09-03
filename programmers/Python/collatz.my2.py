
# While 문을 통해 num과 count 가 특정 값이 될 때까지 루프.
# 3항 연산자 이용해서 num 값 변환
# while 문의 조건식은 true 일때 계속 진행한다 이다. 될때까지 가 아니다.
def solution(num):
    count = 0
    while(num != 1):
        num = num/2 if num % 2 == 0 else num*3+1
        count += 1
        if count == 500:
            count = -1
            break
    return count
