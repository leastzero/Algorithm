import sys
input = sys.stdin.readline

v = list(map(int, input().split()))
answer = 'mixed'

isAscending = True
isDescending = True

for i in range(0, 8):
    if i+1 != v[i]:
        isAscending = False
    if 8-i != v[i]:
        isDescending = False

if isAscending:
    answer = 'ascending'
if isDescending:
    answer = 'descending'
print(answer)