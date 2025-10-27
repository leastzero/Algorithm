from collections import deque

n, m = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
weights = deque(weights)
count = 0

while weights:
    if len(weights) == 1:
        count += 1
        break
    if weights[0] + weights[-1] > m:
        weights.pop()
        count += 1
    else:
        weights.popleft()
        weights.pop()
        count += 1
        
print(count)