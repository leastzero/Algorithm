import itertools

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

combi_numbers = list(itertools.combinations(numbers, 3))
sum_numbers = []

for value in combi_numbers:
    sum_numbers.append(sum(value))

sum_numbers.sort(reverse=True)
print(sum_numbers[K-1])