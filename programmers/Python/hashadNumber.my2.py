# number 를 string 값을 만듦
# string 의 len 만큼 반복문으로 string 각 자리수를 더함
# return 값에 hashad 판별 값 출력

def solution(number):
    string = str(number)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    return (number % sum) == 0
