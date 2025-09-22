import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
set_arr = sorted(set(arr))

dic = { set_arr[i]: i for i in range(len(set_arr))}

for x in arr:
    print(dic[x], end=' ')