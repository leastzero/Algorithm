s = input()
h = 0
for x in s:
    if x == 'A' or x == 'B' or x == 'C':
        h += 3
    elif x == 'D' or x == 'E' or x == 'F':
        h += 4
    elif x == 'G' or x == 'H' or x == 'I':
        h += 5
    elif x == 'J' or x == 'K' or x == 'L':
        h += 6
    elif x == 'M' or x == 'N' or x == 'O':
        h += 7
    elif x == 'P' or x == 'Q' or x == 'R' or x == 'S':
        h += 8
    elif x == 'T' or x == 'U' or x == 'V':
        h += 9
    else:
        h += 10

print(h)