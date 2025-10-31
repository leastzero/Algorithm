T = int(input())

for i in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    
    max_profit = 0
    max_price = 0
    
    for j in price[::-1]:
        if j >= max_price:
            max_price = j
        else:
            max_profit += max_price - j
   
    print("#%d %d" % (i, max_profit))