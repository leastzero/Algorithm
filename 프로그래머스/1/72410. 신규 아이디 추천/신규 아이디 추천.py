def solution(new_id):
    remain_char = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    filter_id = ''
    
    new_id = new_id.lower()
    for x in new_id:
        if x in remain_char:
            filter_id += x
    
    while '..' in filter_id:
        filter_id = filter_id.replace('..', '.')
    
    filter_id = filter_id.strip('.')
        
    if not filter_id:
        filter_id = 'a'
        
    if len(filter_id) >= 16:
        filter_id = filter_id[:15]
        filter_id = filter_id.strip('.')
            
    while len(filter_id) <= 2:
        filter_id += filter_id[-1]
        
    return filter_id