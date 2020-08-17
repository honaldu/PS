# 세 수를 받고 곱한 뒤 string 한 후 string 의 count 함수 이용하여 반복문.

a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
for i in range(0, 10):
    print(d.count(str(i)))
