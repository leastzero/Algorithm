a, b = map(int, input().strip().split(' '))
for i in range(b):
    answer = ''
    for j in range(a):
        answer += '*'
    print(answer)