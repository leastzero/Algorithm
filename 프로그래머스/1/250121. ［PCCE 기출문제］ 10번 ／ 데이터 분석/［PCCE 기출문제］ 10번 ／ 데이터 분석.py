def solution(data, ext, val_ext, sort_by):
    answer = []
    dict_data = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    for x in data:
        if x[dict_data[ext]] < val_ext:
            answer.append(x)
            
    answer.sort(key=lambda x: x[dict_data[sort_by]])
    return answer