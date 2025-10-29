postfix = input()
stack = []

for x in postfix:
    if x.isdecimal():
        stack.append(int(x))
    elif x == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b + a)
    elif x == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif x == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)
    elif x == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)

print(stack[0])