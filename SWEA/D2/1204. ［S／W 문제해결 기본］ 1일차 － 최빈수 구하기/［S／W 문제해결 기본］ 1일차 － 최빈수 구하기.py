t = int(input())
for i in range(1, t+1):
    text = int(input())
    scores = list(map(int, input().split()))
    dict = {}

    for score in scores:
        dict[score] = dict.get(score, 0) + 1

    sorted_dict = sorted(dict.items(), key = lambda item: (item[1], item[0]), reverse=True)
    answer = sorted_dict[0][0]

    print("#%d %d" % (i, answer))