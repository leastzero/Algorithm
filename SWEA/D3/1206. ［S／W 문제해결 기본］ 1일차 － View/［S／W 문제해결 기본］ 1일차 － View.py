for i in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    household = 0

    for j in range(2, n-2):
        slice_height = height[j-2:j+3]
        max_height = max(slice_height)
        if height[j] == max_height:
            slice_height.sort(reverse=True)
            household += slice_height[0] - slice_height[1]

    print("#%d %d" % (i, household))