import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    answer = ''
    for i in range(1, n+1):
        if i % 5 == 0:
            answer = answer.replace('||||', '++++ ')
        else:
            answer += '|'
    print(answer)