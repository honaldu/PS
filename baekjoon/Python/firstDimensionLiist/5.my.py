# 두개의 input 을 받은 후 두번째 점수 p 의 합계에 p의 쵀대값을 나누고 100을 곱한 후 a 로 평균을 냄.

a = int(input())
*p, = map(int, input().split())
print(sum(p)/max(p)*100/a)
