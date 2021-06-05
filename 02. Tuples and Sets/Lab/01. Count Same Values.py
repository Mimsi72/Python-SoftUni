numbers = tuple([float(el) for el in input().split()])

result = []
for num in numbers:
    result.append(F"{num} - {numbers.count(num)}")

output = set(result)
for el in output:
    print(F"{el} times")
