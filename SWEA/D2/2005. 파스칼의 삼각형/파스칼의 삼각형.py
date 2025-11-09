t = int(input())
for i in range(1, t+1):
    n = int(input())
    triangle = []
    print("#%d" % i)

    for row in range(n):
        current_row = [0] * (row + 1)

        current_row[0] = 1
        current_row[-1] = 1

        if row >= 2:
            prev = triangle[-1]
            for j in range(1, row):
                current_row[j] = prev[j-1] + prev[j]

        triangle.append(current_row)

    for row in triangle:
        print(*row)