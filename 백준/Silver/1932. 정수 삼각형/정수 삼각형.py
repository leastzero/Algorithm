import sys
input = sys.stdin.readline

n = int(input())
triangles = []
for _ in range(n):
    triangle = list(map(int, input().split()))
    triangles.append(triangle)

for i in range(1, n):
    for j in range(len(triangles[i])):
        if j == 0:
            triangles[i][j] += triangles[i-1][j]
        elif j == len(triangles[i]) - 1:
            triangles[i][j] += triangles[i-1][j-1]
        else:
            triangles[i][j] += max(triangles[i-1][j-1], triangles[i-1][j]) 

print(max(triangles[n-1]))