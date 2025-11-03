import sys
input = sys.stdin.readline

def DFS(L):
    global count
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        count += 1
        print()
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0] * m
    count = 0
    DFS(0)
    print(count)