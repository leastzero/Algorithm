import sys
from collections import deque

n = int(input())
Q = deque()

for i in range(1, n+1):
    Q.append(i)

while len(Q) != 1:
    Q.popleft()
    num = Q.popleft()
    Q.append(num)

print(Q.popleft())