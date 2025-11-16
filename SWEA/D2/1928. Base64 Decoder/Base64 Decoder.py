Base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

t = int(input())
for i in range(1, t+1):
    encoding = input()
    answer = ''
    bit6 = ''

    for x in encoding:
        bit6 += format(Base64.index(x), '06b')

    n = len(bit6)
    for j in range(0, n, 8):
        bit8 = int(bit6[j:j+8], 2)
        answer += chr(bit8)

    print("#%d %s" % (i, answer))