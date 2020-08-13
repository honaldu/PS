# 빈 공백에 n 의 숫자를 기준으로 반복문을 만들고 반복문의 변수에 따라 빈 string 에 별과 공백 더해줌.
# map 함수로 print 묶어준 다음 unpacking
n = int(input())
a = ""
b = ""

for i in range(1, n+1):
    if (i % 2 == 0):
        b += " *"
    else:
        a += "* "

[*map(print, (a, b)*n)]
print(map(print, (a, b)*n))
