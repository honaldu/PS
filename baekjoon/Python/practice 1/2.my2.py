# 햄버거, 콜라 리스트를 하나씩 만든 후 list min 함수를 통해서 list 최소값을 각가 더하고 빼준다.
A = []
B = []
for i in range(3):
    price = int(input())
    A.append(price)
for i in range(2):
    price = int(input())
    B.append(price)

print(min(A)+min(B)-50)
