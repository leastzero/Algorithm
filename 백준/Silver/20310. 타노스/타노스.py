import sys
input = sys.stdin.readline

s = input()

zero = s.count('0') // 2
one = s.count('1') // 2

s_list = list(s)
cnt_zero = 0
cnt_one = 0

# 0 제거
for i in range(len(s_list)-1, -1, -1): # 뒤에서부터 0 제거 (사전순이니까)
    if s_list[i] == '0':
        s_list[i] = ''
        cnt_zero += 1

        if cnt_zero == zero:
            break

# 1 제거
for i in range(len(s_list)): # 앞에서부터 1 제거 (사전순이니까)
    if s_list[i] == '1':
        s_list[i] = ''
        cnt_one += 1

        if cnt_one == one:
            break

print(''.join(s_list))