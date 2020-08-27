# exec 의 활용. int(input()) 만큼 b *c 실행
# format 함수 안에서 c 요소에 b 만큼 곱한 후 sum(c) 값을 넘는 c요소의 합을 b 만큼 나눔
# format 함수로 소수점 3자리 까지 표시
exec(int(input())*'b,*c=map(int,input().split());print(format(sum(b*i>sum(c)for i in c)/b," .3%"));')
