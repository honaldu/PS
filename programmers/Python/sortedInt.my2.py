# string 은 이터러블로 안 하고 바로 list 로 list 화 가능.

# str 된 n list 함수로 바로 list 화.


def solution(n):

    numberList = reversed(sorted(list(str(n))))
    return int("".join(numberList))
