n = int(input())
player = []
count = 0

for _ in range(n):
    height, weight = map(int, input().split())
    player.append((height, weight))

player.sort(reverse=True)
max_weight = 0

for h, w in player:
    if max_weight < w:
        max_weight = w
        count += 1

print(count)