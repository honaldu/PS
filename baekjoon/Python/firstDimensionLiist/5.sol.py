# * 을 이용하여 a, p 분리. open 함수 인자에 0으로 버퍼링 x, read 함수로 파일 전체 내용 하나 문자열로 읽어 옴.

a, *p, = map(int, open(0).read().split())
print(sum(p)/max(p)*100/a)
