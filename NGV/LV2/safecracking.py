import sys
input = sys.stdin.readline

w, n = map(int, input().split())
jewels = []
for _ in range(n):
    m, p = map(int, input().split())
    jewels.append((m, p))

jewels.sort(key=lambda x: x[1], reverse=True)

total_value = 0
current_weight = 0

for weight, value in jewels:
    remain_weight = w - current_weight

    if weight <= remain_weight:
        total_value += weight * value
        current_weight += weight
    else:
        value_to_add = remain_weight * value
        total_value += value_to_add
        current_weight += remain_weight
        break
    
print(total_value)