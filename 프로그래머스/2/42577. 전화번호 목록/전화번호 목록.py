def solution(phone_book):
    answer = True
    hash = set(phone_book)
    
    for x in phone_book:
        for i in range(1, len(x)):
            prefix = x[:i]
            if prefix in hash:
                answer = False
    return answer