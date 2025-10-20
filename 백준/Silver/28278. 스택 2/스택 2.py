import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    order = list(map(int, sys.stdin.readline().split()))
    if len(order) == 2:
        stack.append(order[1])
    else:
        if order[0] == 2:
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)
        elif order[0] == 3:
            print(len(stack))
        elif order[0] == 4:
            if len(stack) != 0:
                print(0)
            else:
                print(1)
        else:
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)