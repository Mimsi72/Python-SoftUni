n = int(input())

matrix = []
for row in range(n):
    matrix.append(list(input()))

symbol = input()
positions = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            positions = (row, col)
            break
    if positions:
        break

print (positions if positions else F"{symbol} does not occur in the matrix")
