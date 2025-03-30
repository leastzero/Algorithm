n = int(input())
a = 2
for i in range(2*n):
    if i < n:
        blank = " " * (n-i-1)
        star = "*" * (2 * i + 1)
        print("%s%s" % (blank, star))
    else:
        blank = " " * (i - n + 1)
        star = "*" * (2 * n - 1 - a)
        print("%s%s" % (blank, star))
        a += 2