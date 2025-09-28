import sys

n = int(sys.stdin.readline())
answer = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        answer.append(command[1])
    elif command[0] == 'pop':
        if not answer:
            print(-1)
        else:
            print(answer.pop())
    elif command[0] == 'size':
        print(len(answer))
    elif command[0] == 'empty':
        if not answer:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if not answer:
            print(-1)
        else:
            print(answer[-1])