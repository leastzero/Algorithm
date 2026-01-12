import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    answer = 0
    lt, rt = 0, len(cards) - 1

    while lt <= rt:
        mid = (lt + rt) // 2

        if number == cards[mid]:
            answer = 1
            break
        elif number > cards[mid]:
            lt = mid + 1
        else:
            rt = mid -1

    print(answer, end=' ')