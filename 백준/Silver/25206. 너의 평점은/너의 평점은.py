sum = 0
hap = 0
for _ in range(20):
    study, score, grade = input().split()
    score = float(score)
    if grade == 'A+':
        sum += 4.5 * score
    elif grade == "A0":
        sum += 4.0 * score
    elif grade == "B+":
        sum += 3.5 * score
    elif grade == "B0":
        sum += 3.0 * score
    elif grade == "C+":
        sum += 2.5 * score
    elif grade == "C0":
        sum += 2.0 * score
    elif grade == "D+":
        sum += 1.5 * score
    elif grade == "D0":
        sum += 1.0 * score
    elif grade == "F":
        sum += 0.0 * score
    else:
        continue
    hap += score

print(sum / hap)