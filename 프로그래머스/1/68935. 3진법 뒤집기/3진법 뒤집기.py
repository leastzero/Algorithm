def solution(n):
    answer = ''
    while n > 0:
        n, reminder = divmod(n, 3)
        answer += str(reminder)
    answer = int(answer, 3)
    return answer