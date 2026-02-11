import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if arr:
            answer = heapq.heappop(arr)
            print(answer)
        else:
            print(0)
    else:
        heapq.heappush(arr, x)