# for 문을 통한 덧셈
# 배열을 만들고 그 안에 담은 뒤 return

def solution(arr1, arr2):
    procession = []
    for j in range(len(arr1)):
        procession.append([(arr1[j][i] + arr2[j][i])
                           for i in range(len(arr1[0]))])
    return procession
