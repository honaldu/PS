# input 1개와 변수 oxQuiz는 *로 인풋 5개를 받은 뒤 변수는 두개를 둬 하나는 더해질 수, 하나는 O,X 를 만날 시 변하는 값으로 둔다. for in 문을 통해 각 oxQuiz 루프
# oxQuiz 각 문에 반목문안에서 if 문을 통해 String[index] 에서 O,X 를 나눈다.

number = int(input())
strings = [input() for i in range(number)]
finalNumber = 0
changingNumber = 0

for i in strings:
    for j in range(len(i)):
        if(i[j] == 'X'):
            changingNumber = 0
        if(i[j] == 'O'):
            changingNumber += 1
            finalNumber += changingNumber
    print(finalNumber)
    finalNumber = 0
    changingNumber = 0
