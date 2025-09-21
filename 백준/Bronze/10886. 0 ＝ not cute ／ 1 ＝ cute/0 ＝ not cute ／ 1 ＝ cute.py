v = int(input())
vote = []

for _ in range(v):
    vote.append(int(input()))

if vote.count(1) > vote.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")