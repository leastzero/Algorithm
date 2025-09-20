import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sum = 0
min = 0

arr.sort()

for i in range(len(arr)):
    sum += arr[i]
    min += sum

print(min)