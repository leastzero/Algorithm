t = int(input())
for i in range(1, t+1):
    fh, fm, sh, sm = map(int, input().split())

    if fh + sh > 12:
        hour = (fh + sh) - 12
    else:
        hour = fh + sh

    if fm + sm >= 60:
        hour += 1
        minute = (fm + sm) - 60
    else:
        minute = fm + sm

    print("#%d %d %d" % (i, hour, minute))