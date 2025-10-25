def Minute(capacity):
    sum_minute = 0
    count = 1

    for x in length:
        if sum_minute + x > capacity:
            count += 1
            sum_minute = x
        else:
            sum_minute += x

    return count

n, m = map(int, input().split())
length = list(map(int, input().split()))
maxx = max(length)
lt, rt = 1, sum(length)
answer = 0

while lt <= rt:
    mid = (lt + rt) // 2

    if mid >= maxx and Minute(mid) <= m:
        answer = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(answer)