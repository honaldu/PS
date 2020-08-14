# 뗄감 방법. 일일히 input 값 받은 후 list에 넣은 뒤 최대값과 최대값의 index 찾기

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

number = [a, b, c, d, e, f, g, h, i]
print(max(number))
print(number.index(max(number))+1)
