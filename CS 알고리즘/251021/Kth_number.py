T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    slice_numbers = numbers[s-1:e]
    slice_numbers.sort()

    print("#%d %d" % (i+1, slice_numbers[k-1]))