for _ in range(1, 11):
    t = int(input())
    find = input()
    s = input()
    answer = 0

    answer = s.count(find)

    print("#%d %d" % (t, answer))