n, m = map(int, input().split())
dice_sum = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        if i+j in dice_sum:
            dice_sum[i + j] += 1
        else:
            dice_sum[i + j] = 1
            
for key, value in dice_sum.items():
    if max(dice_sum.values()) == value:
        print(key, end=' ')