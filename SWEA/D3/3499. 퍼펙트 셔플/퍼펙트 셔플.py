from collections import deque

t = int(input())
for i in range(1, t+1):
    n = int(input())
    cards = list(input().split())

    answer = []
    if n % 2 == 0:
        first = cards[:n//2]
        second = cards[n//2:]
    else:
        first = cards[:n//2+1]
        second = cards[n//2+1:]

    first = deque(first)
    second = deque(second)

    while True:
        if first:
            answer.append(first.popleft())
        if second:
            answer.append(second.popleft())

        if not first and not second:
            break

    print("#%d" % i, end=' ')
    for x in answer:
        print(x, end=' ')
    print()