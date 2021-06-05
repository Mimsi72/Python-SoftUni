from collections import deque


def create_blank_matrix(row_size, col_size):
    matrix = []
    for _ in range(row_size):
        matrix.append([])
        for _ in range(col_size):
            matrix[-1].append('')

    return matrix


rows, cols = [int(el) for el in input().split(' ')]
text = input()
main_matrix = create_blank_matrix(rows, cols)
idx = 0
col = 0
for row in range(rows):
    dir = -1
    if row % 2 == 0:
        dir = 1

    while 0 <= col < cols:
        snake_pos = row, col
        main_matrix[row][col] = text[idx]
        if idx + 1 == len(text):
            idx = -1
        idx += 1
        col += dir
    col -= dir
for i in range(len(main_matrix)):
    print(''.join(main_matrix[i]))
# snake = deque(list(input()))
# matrix = []
# for row in range(rows):
#     for col in range(cols):
#         if (row + 1) % 2 != 0:
#             element = snake.popleft()
#             matrix.append(element)
#             snake.append(element)
#         else:
#             element = snake.popleft()
#             matrix.appendleft(element)
#             snake.append(element)
# print(matrix)
