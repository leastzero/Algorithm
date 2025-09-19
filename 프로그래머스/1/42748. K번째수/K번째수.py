def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sub_array = array[commands[i][0]-1:commands[i][1]]
        sub_array.sort()
        answer.append(sub_array[commands[i][2]-1])
    return answer