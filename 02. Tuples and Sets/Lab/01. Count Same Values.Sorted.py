numbers = tuple([float(el) for el in input().split()])

result = []
for num in numbers:
    result.append(F"{num} - {numbers.count(num)}")

output = []
for el in result:
    if el not in output:
        output.append(el)
for el in output:
    print(F"{el} times")
