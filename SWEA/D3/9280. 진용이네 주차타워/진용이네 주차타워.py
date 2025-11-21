from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    charges = [int(input()) for _ in range(n)]
    weights = [int(input()) for _ in range(m)]
    orders = [[0, 0] for _ in range(n)]
    answer = 0
    wait_queue = deque()

    for _ in range(2*m):
        order = int(input())
        if order > 0:
            isParked = False
            for i in range(n):
                if orders[i][0] == 0:
                    orders[i][0] = order
                    orders[i][1] = weights[order-1] * charges[i]
                    isParked = True
                    break
            if not isParked:
                wait_queue.append(order)
        else:
            empty = -1
            for i in range(n):
                if orders[i][0] == -1 * order:
                    orders[i][0] = 0
                    answer += orders[i][1]
                    orders[i][1] = 0
                    empty = i
                    break
            if empty != -1 and wait_queue:
                next_car = wait_queue.popleft()
                orders[empty][0] = next_car
                orders[empty][1] = weights[next_car-1] * charges[empty]

    print("#%d %d" % (tc, answer))