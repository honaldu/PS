# 이터러블 이용.


def solution(n):
    number = 0
    for i in range(2, n+1):
        num = 0
        for l in range(2, i):
            if (i % l != 0):
                num += 1
            if (l == (i-1)):
                if (num == 0):
                    number += 1
    print(number)


solution(3)
