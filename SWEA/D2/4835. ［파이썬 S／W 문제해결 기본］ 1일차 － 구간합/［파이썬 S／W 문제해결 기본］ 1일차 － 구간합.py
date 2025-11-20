t = int(input())
for i in range(1, t+1):
    answer = 0
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    min_sum = 1000000000
    max_sum = 0
    for j in range(n-m+1):
        slice_sum = sum(num[j:j+m])
        if slice_sum < min_sum:
            min_sum = slice_sum
        if slice_sum > max_sum:
            max_sum = slice_sum

    answer = max_sum - min_sum

    print("#%d %d" % (i, answer))