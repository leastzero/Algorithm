import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    calculate = sys.stdin.readline().split()

    if len(calculate) == 1:
        if calculate[0] == "all":
            s.update(range(1, 21))
        else:
            s = set()
    else:
        value = int(calculate[1])

        if calculate[0] == "add":
            s.add(value)
        elif calculate[0] == "remove":
            s.discard(value)
        elif calculate[0] == "check":
            if value in s:
                print(1)
            else:
                print(0)
        elif calculate[0] == "toggle":
            if value in s:
                s.discard(value)
            else:
                s.add(value)