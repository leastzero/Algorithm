from collections import deque

required_subject = input()
n = int(input())

for i in range(n):
    plan = input()
    required_subjects = deque(required_subject)

    for x in plan:
        if x in required_subjects:
            if x != required_subjects.popleft():
                print("#%d NO" % (i+1))
                break
    
    else:
        if len(required_subjects) == 0:
            print("#%d YES" % (i+1))
        else:
            print("#%d NO" % (i+1))
