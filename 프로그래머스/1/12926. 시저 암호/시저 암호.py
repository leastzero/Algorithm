def solution(s, n):
    answer = []
    for x in s:
        if x.isalpha():
            if x.isupper():
                answer.append(chr((ord(x) - 65 + n) % 26 + 65))
            elif x.islower():
                answer.append(chr((ord(x) - 97 + n) % 26 + 97))
        else:
            answer.append(' ')
    return "".join(answer)