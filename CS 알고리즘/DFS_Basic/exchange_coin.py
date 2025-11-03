import sys
input = sys.stdin.readline

def DFS(L, sum):
    global min
    if L > min:
        return
    if sum > m:
        return
    
    if sum == m:
        if L < min:
            min = L
    else:
        for i in range(n):
            DFS(L+1, sum + coins[i])

if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    min = 214700000
    coins.sort(reverse=True)
    DFS(0, 0)
    print(min)