n = int(input())
numbers = list(map(int, input().split()))
answer = ''
lt, rt = 0, n-1
last = 0
sequence = []

while lt <= rt:
    if numbers[lt] > last:
        sequence.append((numbers[lt], 'L'))
    if numbers[rt] > last:
        sequence.append((numbers[rt], 'R'))

    sequence.sort()
    if len(sequence) == 0:
        break
    else:
        answer = answer + sequence[0][1]
        last = sequence[0][0]
        if sequence[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    sequence.clear()

print(len(answer))
print(answer)