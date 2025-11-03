t = int(input())
for i in range(1, t+1):
    numbers = list(map(int, input().split()))
    answer = round(sum(numbers) / 10)
    print("#%d %d" % (i, answer))