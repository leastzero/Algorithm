def solution(arr):
    min_num = min(arr)
    arr.remove(min_num)
    
    if not arr:
        arr.append(-1)
        
    return arr