def solution(sizes):
    answer = 0
    w = []
    h = []
    for x in sizes:
        x.sort()
        w.append(x[0])
        h.append(x[1])
    answer = max(w) * max(h)
    return answer