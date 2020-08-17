# print 함수 내부에서 해체작업 한 max()

print(*max((int(input()), i+1)for i in range(9)))
