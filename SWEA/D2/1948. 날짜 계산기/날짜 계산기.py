calender = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

t = int(input())
for i in range(1, t+1):
    fm, fd, sm, sd = map(int, input().split())
    answer = 0

    if fm == sm:
        answer += sd - fd + 1
    else:
        answer += calender[fm] - fd + 1
        answer += sd
        for j in range(fm+1, sm):
            answer += calender[j]

    print("#%d %d" % (i, answer))