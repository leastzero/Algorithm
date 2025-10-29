infix = input()
stack = []
postfix = ''

for x in infix:
    if x.isdecimal():
        postfix += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfix += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
            
while stack:
    postfix += stack.pop()

print(postfix)