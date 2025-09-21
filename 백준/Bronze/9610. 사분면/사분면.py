n = int(input())
arr = [0, 0, 0, 0, 0]

for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        arr[1] += 1
    elif x < 0 and y > 0:
        arr[2] += 1
    elif x < 0 and y < 0:
        arr[3] += 1
    elif x > 0 and y < 0:
        arr[4] += 1
    else:
        arr[0] += 1

print("Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d" % (arr[1], arr[2], arr[3], arr[4], arr[0]))