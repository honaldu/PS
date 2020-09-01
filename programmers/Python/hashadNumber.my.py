# number 를 string 값을 만듦
# string 의 len 만큼 반복문으로 string 각 자리수를 더함
# if 문으로 각 더한 수를 나눠 true/false 값 return

def solution(number):
    string = str(number)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    if((number % sum) == 0):
        return True
    else:
        return False
