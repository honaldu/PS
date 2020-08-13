# input 으로 n 받음
# n 만큼 "* " 을 곱함
# n 을 이용한 string(s) 의 index 만큼 추출
# n 만큼 print 된 map 을 astetik 으로 unpacking

n = int(input())
s = '* '*n
[*map(print, (s[:n], s[1:n+1])*n)]
