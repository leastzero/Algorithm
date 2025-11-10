def DFS(L):
    global min_sum
    if L == n:
        sum = max(person) - min(person)
        if sum < min_sum:
            tmp = set()
            for x in person:
                tmp.add(x)
            if len(tmp) == 3:
                min_sum = sum
    else:
        for i in range(3):
            person[i] += coins[L]
            DFS(L+1)
            person[i] -= coins[L]

if __name__ == "__main__":
    n = int(input())
    coins = []
    person = [0, 0, 0]

    for _ in range(n):
        coin = int(input())
        coins.append(coin)

    min_sum = 214700000
    DFS(0)
    print(min_sum)