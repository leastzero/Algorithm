import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

lt, rt = 1, max(trees)

while lt <= rt:
    mid = (lt + rt) // 2
    total = 0

    for tree in trees:
        if tree > mid:
            total += tree - mid
        if total > m:
            break

    if total >= m:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)