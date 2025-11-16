score = {0: 'A+', 1: 'A0', 2: 'A-', 3: 'B+', 4: 'B0', 5: 'B-', 6: 'C+',
         7: 'C0', 8: 'C-', 9: 'D0'}

t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    answer = ''
    student = []

    for _ in range(n):
        a, b, c = map(int, input().split())
        total = a * 0.35 + b * 0.45 + c * 0.2
        student.append(total)

    num = student[k-1]
    student.sort(reverse=True)
    rank = student.index(num)
    answer = score[rank // (n // 10)]

    print("#%d %s" % (i, answer))