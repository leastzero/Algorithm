n = int(input())
inverse = list(map(int, input().split()))

sequence = [0] * n

for i in range(n):
    for j in range(n):
        if inverse[i] == 0 and sequence[j] == 0:
            sequence[j] = i + 1
            break
        elif sequence[j] == 0:
            inverse[i] -= 1

for x in sequence:
    print(x, end=' ')