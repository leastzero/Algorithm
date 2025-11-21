t = int(input())
for tc in range(1, t+1):
    n, n16 = input().split()
    n10 = int(n16, 16)
    answer = 0
    answer = bin(n10)[2:]
    answer = '0' * (int(n)*4-len(answer)) + answer

    print("#%d %s" % (tc, answer))