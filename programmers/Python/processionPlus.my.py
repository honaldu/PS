# for 문을 통한 덧셈
# python 의 collection 이용한 덧셈?
def solution(arr1, arr2):
    a = []
    b = []
    c = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            a.append(arr1[i][j]+arr2[i][j])
        for j in range(len(arr1[1])):
            b.append(arr1[i][j]+arr2[i][j])
    c.append(a)
    c.append(b)
    return c


solution([[1, 2], [2, 3]]	, [[3, 4], [5, 6]])
