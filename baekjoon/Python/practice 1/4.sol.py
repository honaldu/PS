# 절대값 함수 이용하여 for 1문으로 클리어.

n = int(input())
for i in range(-n+1, n):
    print('*'*(n-abs(i)))
