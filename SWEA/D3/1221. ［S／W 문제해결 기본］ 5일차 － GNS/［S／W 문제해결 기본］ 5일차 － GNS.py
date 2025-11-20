dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

t = int(input())
for i in range(1, t+1):
    tc, n = input().split()
    alpha = list(input().split())
    num = []

    for x in alpha:
        num.append(dic[x])
    num.sort()

    print("#%d" % i)
    for x in num:
        for key, value in dic.items():
            if value == x:
                print(key, end=' ')
                break
    print()