import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    lt, rt = 0, len(a) - 1
    answer = 0
 
    while lt <= rt:
        mid = (lt + rt) // 2

        if number == a[mid]:
            answer = 1
            break
        elif number > a[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    print(answer)