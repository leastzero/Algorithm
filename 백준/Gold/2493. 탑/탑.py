import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))

answer = [0] * n
stack = []

for i in range(n):
    index = i + 1
    height = tower[i]

    while stack:
        top_index, top_height = stack[-1]

        if height < top_height:
            answer[i] = top_index
            break
        else:
            stack.pop()
    stack.append((index, height))

print(*answer)