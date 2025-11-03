import sys

# DFS 문제 풀이
def DFS(L, sum):
    if L == n and sum == f:
        for x in permutation:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                permutation[L] = i
                DFS(L+1, sum+(permutation[L]*binary[L]))
                check[i] = 0

if __name__ == '__main__':
    n, f = map(int, input().split())
    binary = [1] * n
    permutation = [0] * n
    check = [0] * (n+1)

    for i in range(1, n):
        binary[i] = binary[i-1] * (n - i) // i

    DFS(0, 0)


# 라이브러리 문제
import itertools as it

n, f = map(int, input().split())
binary = [1] * n

for i in range(1, n):
    binary[i] = binary[i-1] * (n-i) // i

numbers = list(range(1, n+1))

for tmp in it.permutations(numbers):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x * binary[L])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break