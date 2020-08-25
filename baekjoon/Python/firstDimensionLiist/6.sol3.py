# 첫번쨰 input 변수 안 쓰고 바로 for 에서 사용. input을 X로 split 한 후 등차수열의 합으로 끊긴 부분 합함.

for i in range(int(input())):
    print(sum((len(i)**2+len(i))//2for i in input().split('X')))
