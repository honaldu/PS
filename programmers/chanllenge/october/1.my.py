def solution(n):
    tNum = ''
    while 1 <= n:
        tNum += str(n % 3)
        n = n//3
    return int(tNum, 3)


print(solution(45))
