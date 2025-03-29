s = input()
a = [-1] * 26

for i in range(len(s)):
    if a[ord(s[i]) - 97] == -1:
        a[ord(s[i]) - 97] = i

for x in a:
    print(x, end=" ")