import math

def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 3), 2: (1, 3), 3: (2, 3),
        4: (0, 2), 5: (1, 2), 6: (2, 2),
        7: (0, 1), 8: (1, 1), 9: (2, 1),
        '*': (0, 0), 0: (1, 0), '#': (2, 0)
    }
    left, right = '*', '#'
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            left = x
            answer += 'L'
        elif x == 3 or x == 6 or x == 9:
            right = x
            answer += 'R'
        else:
            x1, y1 = keypad[x]
            x2, y2 = keypad[left]
            x3, y3 = keypad[right]
            if abs(x1 - x2) + abs(y1 - y2) < abs(x1 - x3) + abs(y1 - y3):
                answer += 'L'
                left = x
            elif abs(x1 - x2) + abs(y1 - y2) > abs(x1 - x3) + abs(y1 - y3):
                answer += 'R'
                right = x
            else:
                if hand == 'left':
                    answer += 'L'
                    left = x
                else:
                    answer += 'R'
                    right = x
    return answer