c = int(input())
for i in range(1, c + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]

    isTrue = 0
    sumA, sumB = 0, 0

    code = ""
    found = False
    scanner = {0: "0001101", 1: "0011001", 2: "0010011", 3: "0111101", 4: "0100011",
               5: "0110001", 6: "0101111", 7: "0111011", 8: "0110111", 9: "0001011"}

    for j in range(n-1, -1, -1):
        for k in range(m-1, -1, -1):
            if board[j][k] == '1':
                start_index = k - 55

                if start_index >= 0:
                    code = board[j][start_index: k + 1]
                    found = True
                    break
        if found:
            break

    if found and len(code) == 56:
        index = 1

        for j in range(0, 56, 7):
            cut_code = code[j: j+7]
            k_digit = 0

            for key, value in scanner.items():
                if value == cut_code:
                    k_digit = key
                    break

            if index % 2 == 0:
                sumB += k_digit
            else:
                sumA += k_digit
            index += 1

        if (sumA * 3 + sumB) % 10 == 0:
            isTrue = sumA + sumB

    print("#%d %d" % (i, isTrue))