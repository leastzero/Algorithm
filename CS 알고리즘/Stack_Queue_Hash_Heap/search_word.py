n = int(input())
words = {}

for _ in range(n):
    word = input()
    words[word] = 1

for _ in range(n-1):
    poem = input()
    words[poem] = 0

for key, value in words.items():
    if value == 1:
        print(key)
        break