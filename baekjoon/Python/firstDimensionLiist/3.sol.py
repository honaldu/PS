# exec 함수를 이용하여 n,m 변수 만든 후 m 에 int 3 번 곱한 후 str.count 를 이용하고 count 문 끝날 때 마다 n에 1을 더함

exec('n,m=0,1'+'*int(input())'*3+';print(str(m).count(str(n)));n+=1'*10)
