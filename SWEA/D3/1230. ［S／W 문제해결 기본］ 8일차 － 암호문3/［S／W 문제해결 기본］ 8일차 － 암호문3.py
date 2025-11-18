from collections import deque

for t in range(1, 11):
    n = int(input())
    original = list(input().split())
    m = int(input())
    command = list(input().split())
    Q = deque(command)

    while Q:
        s = []
        com = Q.popleft()
        if com == 'I':
            x = int(Q.popleft())
            y = int(Q.popleft())
            for i in range(y):
                s.append(Q.popleft())
            original = original[:x] + s + original[x:]
        elif com == 'D':
            x = int(Q.popleft())
            y = int(Q.popleft())
            original = original[:x] + original[x+y:]
        elif com == 'A':
            y = int(Q.popleft())
            for i in range(y):
                s.append(Q.popleft())
            original = original + s
    print("#%d" % t, end=' ')
    for i in range(10):
        print(original[i], end=' ')
    print()