n = int(input())

matrix = []

for row in range(n):
    matrix.append(list(input()))

symbol = input()
not_matched = True
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print((row, col))
            not_matched = False
            break
        if not not_matched:
            break

if not_matched:
    print(F"{symbol} does not occur in the matrix")
