n = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / n)
close_scores = []
close_score = max(scores)

for score in scores:
    if abs(avg - score) < close_score:
        close_score = abs(avg - score)

for i in range(n):
    if abs(avg - scores[i]) == close_score:
        close_scores.append((scores[i], i + 1))

close_scores.sort(key=lambda x: (-x[0], x[1]))
print(avg, close_scores[0][1])