# 이터러블 이용.
# 시간초과


def solution(n):
    numbers = [int(i) for i in range(2, n+1)]

    countDown = 0
    for i in numbers:
        count = 0
        for l in range(2, i):
            if i % l == 0:
                count += 1
        if count == 0:
            countDown += 1
    return countDown


solution(5)
