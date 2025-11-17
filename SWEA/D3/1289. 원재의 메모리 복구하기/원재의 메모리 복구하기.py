t = int(input())
for i in range(1, t+1):
    memory = list(map(int, input()))
    answer = 0
    pre_memory = 0

    for j in range(len(memory)):
        if memory[j] != pre_memory:
            answer += 1
            pre_memory = 1 - pre_memory

    print("#%d %d" % (i, answer))