from collections import deque

n, m = map(int, input().split())
danger = [(pos, value) for pos, value in enumerate(list(map(int, input().split())))]
danger = deque(danger)

count = 0

while True:
    patient = danger.popleft()
    if any(patient[1] < x[1] for x in danger):
        danger.append(patient)
    else:
        count += 1
        if patient[0] == m:
            break

print(count)