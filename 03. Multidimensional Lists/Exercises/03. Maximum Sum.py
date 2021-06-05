rows, cols = [int(el) for el in input().split(' ')]

matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split(' ')])

max_matrix = []
max_sum = 0

for row in range(rows - 2):
    sub_matrix = []
    for col in range(cols - 2):
        sub_matrix = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        ]
        current_sum = 0
        for r in range(3):
            for c in range(3):
                current_sum += sub_matrix[r][c]

        if max_sum <= current_sum:
            max_sum = current_sum
            max_matrix = sub_matrix
            current_sum = 0

print(F"Sum = {max_sum}")
for row in range(len(max_matrix)):
    for col in range(len(max_matrix)):
        print(max_matrix[row][col], end=' ')
    print()
