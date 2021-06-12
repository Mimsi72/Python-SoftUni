n, m = [int(el) for el in input().split(' ')]
matrix = []
base = ord('a')

for row in range(n):
    matrix.append([])
    for col in range(m):
        first_line = chr(row + base)
        middle_line = chr(row + col + base)
        matrix[-1].append(f'{first_line}{middle_line}{first_line}')

print('\n'.join(' '.join([str(el) for el in row]) for row in matrix))
