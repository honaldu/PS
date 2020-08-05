# 햄버거, 콜라 리스트를 하나씩 만든 후 리스트 정렬을 통해 가격순으로 리스트 내부를 정렬한 다음 가장 싼 각각을 더하고 50을 빼서 출력한다?
A = []
B = []
for i in range(3):
    price = int(input())
    A.append(price)
for i in range(2):
    price = int(input())
    B.append(price)
A.sort()
B.sort()
print(A[0]+B[0]-50)
