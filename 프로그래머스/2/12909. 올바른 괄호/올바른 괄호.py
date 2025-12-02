from collections import deque

def solution(s):
    answer = True
    stack = []
    Q = deque(s)

    while Q:
        current_s = Q.popleft()
        if current_s == '(':
            stack.append(current_s)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    
    if stack:
        answer = False
    return answer