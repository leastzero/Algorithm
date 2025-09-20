score = input()
answer = 0

if score == "A+":
    answer = 4.3
elif score == "A0":
    answer = 4.0
elif score == "A-":
    answer = 3.7
elif score == "B+":
    answer = 3.3
elif score == "B0":
    answer = 3.0
elif score == "B-":
    answer = 2.7
elif score == "C+":
    answer = 2.3
elif score == "C0":
    answer = 2.0
elif score == "C-":
    answer = 1.7 
elif score == "D+":
    answer = 1.3
elif score == "D0":
    answer = 1.0
elif score == "D-":
    answer = 0.7
else:
    answer = 0.0

print(answer)