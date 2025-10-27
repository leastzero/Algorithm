def Count(len):
    count = 0
    for x in lines:
        count += (x // len)
    return count

k, n = map(int, input().split())
lines = []
largest = 0
answer = 0

for i in range(k):
    length = int(input())
    lines.append(length)
    largest = max(largest, length)

lt, rt = 0, largest

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)