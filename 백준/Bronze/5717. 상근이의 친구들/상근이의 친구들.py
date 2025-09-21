F = M = 1

while F != 0 and M != 0:
    M, F = map(int, input().split())
    if F == M == 0:
        break
    print(M+F)