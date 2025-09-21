t = int(input())

for _ in range(t):
    result = input()
    score = 0
    sum = 0

    for x in result:
        if x == 'O':
            sum += 1
            score += sum
        else:
            sum = 0
            
    print(score)