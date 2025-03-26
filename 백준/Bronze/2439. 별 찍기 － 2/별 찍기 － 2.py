n = int(input())

for i in range(n):
    blank = " " * (n - 1 - i)
    star = "*" * (i + 1)
    print("%s%s" % (blank, star))