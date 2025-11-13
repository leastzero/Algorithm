from collections import deque

t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = []

    QA = deque(a)
    QB = deque(b)

    if n < m:
        while len(QB) >= len(QA):
            hap = 0
            for j in range(n):
                hap += QA[j] * QB[j]
            answer.append(hap)
            QB.popleft()
    elif n > m:
        while len(QA) >= len(QB):
            hap = 0
            for j in range(m):
                hap += QA[j] * QB[j]
            answer.append(hap)
            QA.popleft()
    else:
        for j in range(n):
            hap += QA[j] * QB[j]
        answer.append(hap)

    print("#%d %d" % (i, max(answer)))