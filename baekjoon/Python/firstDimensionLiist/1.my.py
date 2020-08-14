import sys

a = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
print(min(numbers))
print(max(numbers))
