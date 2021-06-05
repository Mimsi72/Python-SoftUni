def read_matrix(rows):
    matrix = []

    for _ in range(rows):
        matrix.append([])
        for el in input().split():
            inner_list = matrix[-1]
            inner_list.append(int(el))

    return matrix


result = 0
n = int(input())
matrix = read_matrix(n)
for row in range(n):
    first_diagonal = matrix[row][row]
    second_diagonal = matrix[row][(n-1) - row]
    result += (first_diagonal - second_diagonal)

print(abs(result))
