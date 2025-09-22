t = int(input())

a = b = c = 0
counta = countb = countc = 0

while True:
    if t - 300 >= 0:
        t -= 300
        counta += 1
    elif t - 60 >= 0:
        t -= 60
        countb += 1
    else:
        t -= 10
        countc += 1

    if t <= 0:
        break

if t != 0:
    print(-1)
else:
    print(counta, countb, countc)