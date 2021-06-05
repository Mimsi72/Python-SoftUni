rows, cols = [int(el) for el in input().split(', ')]

matrix = []
result = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

matrix_max_value = 0
position = None
for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        current_max_value = matrix[row - 1][col - 1] + matrix[row][col] + matrix[row - 1][col] + matrix[row][col - 1]
        if matrix_max_value <= current_max_value:
            matrix_max_value = current_max_value
            position = (row, col)

row, col = position
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 1], matrix[row][col])
print(matrix_max_value)

