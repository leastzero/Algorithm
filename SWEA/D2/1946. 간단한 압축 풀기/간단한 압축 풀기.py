t = int(input())
for i in range(1, t+1):
    n = int(input())
    answer = ''

    for _ in range(n):
        c, k = input().split()
        answer += c * int(k)

    print("#%d" % i)
    for j in range(0, len(answer), 10):
        print(answer[j:j+10])