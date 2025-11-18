t = int(input())
for i in range(1, t+1):
    n = int(input())
    answer = 0
    ms = 0
    for _ in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1:
            ms += command[1]
        elif command[0] == 2:
            if ms < command[1]:
                ms = 0
            else:
                ms -= command[1]
        answer += ms

    print("#%d %d" % (i, answer))