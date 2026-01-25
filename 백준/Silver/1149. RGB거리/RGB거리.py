import sys
input = sys.stdin.readline

n = int(input())
colors = [0]

for _ in range(n):
    r, g, b = map(int, input().split())
    colors.append([r, g, b])

dp = [[0] * (n+1)]
        
for i in range(2, n+1):
    colors[i][0] += min(colors[i-1][1], colors[i-1][2])
    colors[i][1] += min(colors[i-1][0], colors[i-1][2])
    colors[i][2] += min(colors[i-1][0], colors[i-1][1])

print(min(colors[n]))