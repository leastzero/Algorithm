import math

t = int(input())

for _ in range(t):
    A, B = map(int, input().split())
    print(math.lcm(A, B))