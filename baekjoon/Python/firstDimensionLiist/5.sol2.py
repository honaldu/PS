# input 값 하나 받아 온 뒤 a 에서 해결. 평균값도 len(a) 로 해결
input()
*a, = map(int, input().split())
print(sum(a)*100/max(1)/len(a))
