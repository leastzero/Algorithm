n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for s, e in meetings:
    if s >= end_time:
        end_time = e
        count += 1

print(count)