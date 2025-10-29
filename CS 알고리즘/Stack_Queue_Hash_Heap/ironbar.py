iron = input()
stack = []
piece = 0

for i in range(len(iron)):
    if iron[i] == '(':
        stack.append(iron[i])
    else:
        stack.pop()
        if iron[i-1] == '(':
            piece += len(stack)
        else:
            piece += 1

print(piece)