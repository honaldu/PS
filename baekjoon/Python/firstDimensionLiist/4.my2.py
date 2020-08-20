# list 안에 for 반목문으로 input 값 받은 뒤 set 으로 중복 삭제 및 길이
numbers = [int(input()) % 42 for i in range(10)]
print(len(set(numbers)))
