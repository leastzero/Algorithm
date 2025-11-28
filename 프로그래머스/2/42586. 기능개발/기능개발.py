def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        days.append(count)
    
    current_day = days.pop(0)
    count_day = 1
    while days:
        next_day = days.pop(0)
        if current_day >= next_day:
            count_day += 1
        else:
            answer.append(count_day)
            count_day = 1
            current_day = next_day
    answer.append(count_day)
    return answer