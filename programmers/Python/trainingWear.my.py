# 2중 expression 사용
# lost 가 외막
# reserve 내막
# lost +1,-1 한 숫자가 lost reserve 안에 있을 경우 빼고 reserve return 및 lost 에서 된 수 제거
# n 에서 lost 길이 만큼 뺀 수 return

# for 문 사용
# lost, -1,+1 한 값이 reserve 안에 있을시 해당되는 lost 값과 reserve 제거
# n 에서 lost 길이 뺀 수 return

def solution(n, lost, reserve):
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
        elif i-1 in reserve:
            reserve.remove(i-1)
        lost.remove(i)
    return n-len(lost)


print(solution(4, [2], [1]))
