n = int(input())
nums = [str(i) for i in range(1, n+1)]

for num in nums:
    count = 0
    count += num.count('3')
    count += num.count('6')
    count += num.count('9')

    if count > 0:
        print('-' * count, end=' ')
    else:
        print(num, end=' ')