count = [int(x) for x in input().split()]

matrix = []

#       get matrix
for i in range(count[0]):
    matrix.append([x for x in input().split()])

action = input().split()

printer = False
while not action[0] == "END":
    if action[0] == "swap" and len(action) == 5:
        row1, col1, row2, col2 = (int(x) for x in action[1:5])
        if row1 < count[0] and col1 < count[1] and row2 < count[0] and col2 < count[1]:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for i in range(count[0]):
                for j in range(count[1]):
                    print(matrix[i][j], end=" ")
                print()
        else:
            printer = True
    else:
        printer = True
    if printer:
        print("Invalid input!")
        printer = False
    action = input().split()
