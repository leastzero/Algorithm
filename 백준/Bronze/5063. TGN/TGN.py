t = int(input())

for _ in range(t):
    answer = ""
    r, e, c = map(int, input().split())
    if e - c > r:
        answer = "advertise"
    elif e - c == r:
        answer = "does not matter"
    else:
        answer = "do not advertise"
    print(answer)