#1 첫번째 방법 (딕셔너리 해쉬)
first = input()
second = input()

words = {}

for x in first:
    words[x] = words.get(x, 0) + 1

for x in second:
    words[x] = words.get(x, 0) - 1

for x in first:
    if words.get(x) > 0:
        print("NO")
        break
else:
    print("YES")


# 두번째 방법 (리스트 해쉬)
first = input()
second = input()

words_first = [0] * 52
words_second = [0] * 52

for x in first:
    if x.isupper():
        words_first[ord(x) - 65] += 1
    else:
        words_first[ord(x) - 71] += 1

for x in second:
    if x.isupper():
        words_second[ord(x) - 65] += 1
    else:
        words_second[ord(x) - 71] += 1

for i in range(52):
    if words_first[i] != words_second[i]:
        print("NO")
        break
else:
    print("YES")