# 2중 for 문 으로 input 으로 받은 n을 기준 삼아 공백과 별 출력

n = int(input())

for i in range(1, n+1):
    for j in range(1, n//2):
        print("*"*(j)+" "*(j-1))
