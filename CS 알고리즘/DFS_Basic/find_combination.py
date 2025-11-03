import sys
input = sys.stdin.readline

def DFS(L, s):
    global count
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        count += 1
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)       

if __name__ == '__main__':
    n, m = map(int, input().split())

    res = [0] * (n + 1)
    count = 0

    DFS(0, 1)

    print(count)