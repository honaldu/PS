# or 연산자로 빈 배열 일 시 [-1] return

def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
   
print(solution([3,2,6],10))