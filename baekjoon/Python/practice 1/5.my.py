# 절대값 반복문을 이용하여 앞 뒤의 공백을 더하고 별을 그린다
# 출력 오류 남
# 백준 문제였다. 코드는 문제 없음

n = int(input())

for i in range(-n+1, n):
    print(" "*abs(n-1-abs(i))+"*"*abs(abs(2*i)+1))
