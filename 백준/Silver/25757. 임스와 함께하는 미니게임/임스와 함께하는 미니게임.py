n, game = input().split()
n = int(n)
persons = []
count = 0

for _ in range(n):
    person = input()
    persons.append(person)

persons = set(persons)

if game == 'Y':
    while len(persons) >= 1:
        persons.pop()
        count += 1
elif game == 'F':
    while len(persons) >= 2:
        persons.pop()
        persons.pop()
        count += 1
else:
    while len(persons) >= 3:
        persons.pop()
        persons.pop()
        persons.pop()
        count += 1

print(count)