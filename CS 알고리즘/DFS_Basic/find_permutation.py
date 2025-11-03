import sys
input = sys.stdin.readline

def DFS(L):
    global count
    if L == m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        count += 1
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                res[L] = i
                check[i] = 1
                DFS(L + 1)
                check[i] = 0         

if __name__ == '__main__':
    n, m = map(int, input().split())

    check = [0] * (n + 1)
    res = [0] * m
    count = 0

    DFS(0)

    print(count)