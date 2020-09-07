N = int(input())
plan = [input().split()]
rule = ['L', 'R', 'U', 'D']
rowColumn = []
row = [[i for i in range(1, N+1)] for j in range(N)]
startRow, startColumn = 1
for i in plan:
    if(i == rule[0]):
        if startRow < 1:
            continue
        else:
            startRow -= 1
    if(i == rule[1]):
        if startRow > N:
            continue
        else:
            startRow += 1
    if(i == rule[2]):
        if startColumn < 1:
            continue
        else:
            startColumn -= 1
    if(i == rule[3]):
        if startColumn > N:
            continue
        else:
            startColumn += 1
print(rowColumn[startColumn][startRow])
