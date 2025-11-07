def DFS(L):
    global max_num
    if L == change:
        max_num = max(max_num, int(''.join(nums)))
        return
    else:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                if (L, int(''.join(nums))) not in check:
                    check.append((L, int(''.join(nums))))
                    DFS(L+1)
                nums[i], nums[j] = nums[j], nums[i]


t = int(input())
for i in range(1, t+1):
    num, change = map(int, input().split())
    nums = list(str(num))
    check = []

    max_num = 0
    DFS(0)
    print("#%d %d" % (i, max_num))