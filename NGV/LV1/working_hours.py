import sys
input = sys.stdin.readline

answer = 0
for _ in range(5):
    start, end = input().split()
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))

    if end_m < start_m:
        end_h -= 1
        end_m = 60 + end_m
    
    hour = end_h - start_h
    minute = end_m - start_m
    answer += (hour * 60) + minute

print(answer)