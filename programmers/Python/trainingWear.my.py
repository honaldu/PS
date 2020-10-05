# 2중 expression 사용
# lost 가 외막
# reserve 내막
# lost +1,-1 한 숫자가 lost reserve 안에 있을 경우 빼고 reserve return 및 lost 에서 된 수 제거
# n 에서 lost 길이 만큼 뺀 수 return

# for 문 사용
# lost, -1,+1 한 값이 reserve 안에 있을시 해당되는 lost 값과 reserve 제거
# n 에서 lost 길이 뺀 수 return

def solution(n, lost, reserve):
    for number in lost:
        if number in reserve:
            reserve.remove(number)
            lost.remove(number)
            continue
        elif number-1 in reserve:
            reserve.remove(number-1)
            lost.remove(number)
            continue
        elif number+1 in reserve:
            reserve.remove(number+1)
            lost.remove(number)
            continue
    return n-len(lost)


print(solution(5, [2, 4], [1, 3, 5]))
