def Count(distance):
    count = 1
    ep = stables[0]
    for i in range(1, n):
        if stables[i] - ep >= distance:
            count += 1
            ep = stables[i]
    return count

n, c = map(int, input().split())
stables = []
answer = 0

for _ in range(n):
    x = int(input())
    stables.append(x)

stables.sort()
lt, rt = 1, stables[-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)