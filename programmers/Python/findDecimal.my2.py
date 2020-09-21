# 마지막까지 포기 하지 말기
# 기존의 방법이 틀렸다면 새로운 방법을 구글링해서 찾아내야 한다.
# 이터러블에 대한 집착 보다 자료형과 팩토링에 대한 집착이 중요.

# 방법을 찾아도 되지만 그 방법을 구현해야 함.

# set 함수의 마이너스 api 이용 구현.

# 아리스토테네스의 체 구현.

def solution(n):
    # set 으로 집합형 자료 생성
    num = set(range(2, n+1))
    for i in range(2, n+1):
        # i 가 num 안에 있을 시
        if i in num:
            # num 에서 2*i 에서 시작해 n 까지 i씩 더해지는 set 을 뺀다.
            # i 자신을 제외한 i 의 배수 삭제.
            num -= set(range(2*i, n+1, i))
    return len(num)


solution(10)
