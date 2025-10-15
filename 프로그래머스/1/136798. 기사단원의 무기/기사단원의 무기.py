def solution(number, limit, power):
    divisor = []
    sum = 0
    
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if j * j == i:
                count += 1
                continue
            if i % j == 0:
                count += 2
        divisor.append(count)
            
    for i in divisor:
        if i > limit:
            sum += power
        else:
            sum += i
            
    return sum