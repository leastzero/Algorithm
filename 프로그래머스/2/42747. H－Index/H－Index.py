def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        h_candidate = i + 1
        if citations[i] >= h_candidate:
            answer = h_candidate
        else:
            break
    return answer