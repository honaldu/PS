# 하나의 list 생성 후 반복문으로 42로 나눈 input 값 넣은 후 list 에 set하고 다시 list 로 바꾼 후 list 길이 print
numbers = []

for i in range(10):
    number = int(input()) % 42
    numbers.append(number)

formedNumbers = list(set(numbers))

print(len(formedNumbers))
