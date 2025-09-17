t = int(input())

for _ in range(t):
    arr = list(map(str, input().split()))
    answer = float(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == "@":
            answer *= 3
        elif arr[i] == "%":
            answer += 5
        else:
            answer -= 7
    print("%0.2f" % answer)