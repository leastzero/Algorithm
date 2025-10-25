# 기본 풀이
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for i in range(len(numbers)):
    if numbers[i] == m:
        answer = i + 1
        break

print(answer)

# 이분 검색 풀이
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

lt, rt = 0, n-1

while lt <= rt:
    mid = (lt + rt) // 2
    if numbers[mid] == m:
        print(mid + 1)
        break
    elif numbers[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1