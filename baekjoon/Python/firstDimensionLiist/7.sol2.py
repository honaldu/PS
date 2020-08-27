# for 문을 ㅑnt(input()) 만큼 받음
# sum 함수는 list 안에 조건이 맞는 것의 요소의 수를 나타냄.
# '%.3f%%' 로 소수점 3자리 까지 남김.
# my1 의 count 과정을 sum 에서 해결.

for T in range(int(input())):
    n, *l = map(int, input().split())
    s = sum(l)/n
    print('%.3f%%' % (sum(i > s for i in l)*100/n))
