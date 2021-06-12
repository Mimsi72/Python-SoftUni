line = input().split(', ')
output = (f'{x} -> {len(x)}' for x in line)
print(', '.join(output))
