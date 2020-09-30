def solution(a,b):
    basic = 2
    month = None
    date = None
    if a==(1 or 10):
        month = 1
    elif a == (2 or 3):
        month = 4
    elif a == 4 :
        month = 7
    elif a ==5 :
        month = 2
    elif a == 6:
        month = 5
    
    return month

print(solution(10,10))