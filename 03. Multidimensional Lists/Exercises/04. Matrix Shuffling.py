rows, cols = [int(el) for el in input().split(' ')]

matrix = []
for row in range(rows):
    matrix.append([el for el in input().split(' ')])

command = input()
while command != "END":
    try:
        swap, row1, col1, row2, col2 = command.split()
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)

        if swap == "swap" and row1 in range(rows) and col1 in range(cols) and row2 in range(rows) and col2 in range(cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for r in range(rows):
                for c in range(cols):
                    print(matrix[r][c], end=' ')
                print()
        else:
            print("Invalid input!")

    except ValueError:
        print("Invalid input!")
    command = input()
