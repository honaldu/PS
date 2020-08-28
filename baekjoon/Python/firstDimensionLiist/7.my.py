# for 문으로 첫줄 input 만큼 input값 받음
# input 값 * 로 a 와 p 배열 분리
# p 배열 내에서 평균 값 넘는 요소 있을 시 count 1 씩 올림
# 출력 때 소수점 강제로 표시
# 코드 퀄리티? 그럭저럭

for i in range(int(input())):
    a, *p = map(int, input().split())
    s = sum(p)/a
    print('%.3f%%' % (sum(i > s for i in p)*100/a))
