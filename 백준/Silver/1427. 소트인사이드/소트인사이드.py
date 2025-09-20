num = int(input())
sort_num = sorted(list(str(num)), reverse=True)
print(int(''.join(sort_num)))