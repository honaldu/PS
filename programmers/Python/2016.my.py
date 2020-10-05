<<<<<<< HEAD
def solution(a,b):
    share = 16 // 12
    rest = 16%12
    four = rest //4
    sum = share +rest +four

print(solution(3,10))
=======
# 2016년 각 달의 날일 수 list
# 요일 list
# a의 전달 sum 함수로 합계 에 b를 더함
# 더한 수의 나머지로 weakends 의 index 처리
def solution(a, b):

    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weakends = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return weakends[(sum(months[0:a-1])+b) % 7]


print(solution(5, 24))
>>>>>>> a3a1315543217351d99e2fda1711831712b1a759
