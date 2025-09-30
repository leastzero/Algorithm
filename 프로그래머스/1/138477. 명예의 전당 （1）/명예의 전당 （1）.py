def solution(k, score):
    stack = []
    answer = []
    for x in score:
        if len(stack) < k:
            stack.append(x)
        else:
            if x > min(stack):
                stack.pop()
                stack.append(x)
        stack = sorted(stack, reverse=True)
        answer.append(stack[-1])
    return answer