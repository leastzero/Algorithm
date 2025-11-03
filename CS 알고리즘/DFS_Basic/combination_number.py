# DFS 문제풀이
def DFS(L, sum, s):
    global count
    if L == k:
        if sum % m == 0:
            count += 1
    else:
        for i in range(s, n):
            DFS(L+1, sum+numbers[i], i+1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    m = int(input())

    count = 0

    DFS(0, 0, 0)
    print(count)

# 라이브러리 문제 풀이
import itertools as it

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
m = int(input())
count = 0

for tmp in it.combinations(numbers, k):
    if sum(tmp) % m == 0:
        count += 1

print(count)