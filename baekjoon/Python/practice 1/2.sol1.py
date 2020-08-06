# 변수를 받고 변수 만으로 최소, 최대 값을 정했다.

# *(Asterisk) 로 변수값의 3개를 args 하나에 저장. 나머지는 각 변수 대입. eval 함수로 String 값 5번 실행 해서 input 값 받아옴
*p, q, r = eval("int(input()),"*5)
# min 함수로 p 중 최소와 q,r중 최소를 더한 뒤 뺌.
print(min(p)+min(q, r)-50)
