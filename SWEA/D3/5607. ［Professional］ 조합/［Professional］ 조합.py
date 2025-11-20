def power(a, b):
    result = 1
    a %= p

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        b //= 2

    return result

def inverse_mod(n):
    return power(n, p-2)

p = 1234567891
MAX = 1000000
factorial = [1] * (MAX+1)
for i in range(2, MAX+1):
    factorial[i] = (factorial[i-1] * i) % p

t = int(input())
for i in range(1, t+1):
    answer = 0
    n, r = map(int, input().split())
    numerator = factorial[n]
    denominator = (factorial[r] * factorial[n-r]) % p

    inverse_denominator = inverse_mod(denominator)
    answer = (numerator * inverse_denominator) % p

    print("#%d %d" % (i, answer))