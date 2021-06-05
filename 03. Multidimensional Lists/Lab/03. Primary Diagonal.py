n = int(input())

matrix = []
result = 0
for row in range(n):
    matrix.append([int(el) for el in input().split(' ')])
    for col in range(n):
        if row == col:
            result += matrix[row][col]

print(result)
