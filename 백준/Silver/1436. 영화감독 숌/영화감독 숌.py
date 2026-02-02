import sys
input = sys.stdin.readline

n = int(input())
num = 1
answer = 0

while True:
    str_num = str(num)
    if '666' in str_num:
        answer += 1

    if answer == n:
        print(num)
        break
    
    num += 1