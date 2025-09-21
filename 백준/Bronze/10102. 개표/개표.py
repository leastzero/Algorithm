v = int(input())
vote = input()

counta= 0
countb = 0

for x in vote:
    if x == 'A':
        counta += 1
    else:
        countb += 1

if counta > countb:
    print('A')
elif counta == countb:
    print("Tie")
else:
    print('B')