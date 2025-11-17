for t in range(1, 11):
    n = int(input())
    secret = list(input().split())
    command = int(input())
    commands = [x.split() for x in input().split('I')[1:]]

    for com in commands:
        x = int(com[0])
        y = int(com[1])
        s = com[2:]
        secret = secret[:x] + s + secret[x:]

    print("#%d" % t, end=' ')
    print(" ".join(secret[:10]))