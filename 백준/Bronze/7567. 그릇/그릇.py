bowl = input()
answer = 10

for i in range(1, len(bowl)):
    if bowl[i-1] == bowl[i]:
        answer += 5
    else:
        answer += 10

print(answer)