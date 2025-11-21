t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        answer = 1
    else:
        answer = 0

    print("#%d %d" % (tc, answer))