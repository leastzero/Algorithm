t = int(input())

for _ in range(t):
    county = 0
    countk = 0
    for _ in range(9):
        y, k = map(int, input().split())
        county += y
        countk += k
    if county > countk:
        print("Yonsei")
    elif county < countk:
        print("Korea")
    else:
        print("Draw")