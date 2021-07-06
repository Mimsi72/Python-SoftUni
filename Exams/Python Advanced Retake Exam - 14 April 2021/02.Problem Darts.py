players = {}
for player in input().split(', '):
    players[player] = int(501)
throws = 0
matrix_size = 7
matrix = []
for row in range(matrix_size):
    matrix.append([el for el in input().split(' ')])


def corresponding_numbers(r, c, matrix_to_check):
    multiplier = ((int(matrix_to_check[r][0])) + (int(matrix_to_check[r][6])) /
                  + (int(matrix_to_check[0][c])) + (int(matrix_to_check[6][c])))
    return multiplier

    # res = 0
    # corners = [
    #     (r, 0),
    #     (r, 6),
    #     (0, c),
    #     (6, c),
    # ]
    # for corner in corners:
    #     (corner_row, corner_column) = corner
    #     res += int(matrix_to_check[corner_row][corner_column])
    # return res


winner = False

while not winner:
    throws += 1
    for player in players:
        aim = input().lstrip("(").rstrip(")")
        aimed_row, aimed_col = aim.split(', ')
        aimed_row, aimed_col = int(aimed_row), int(aimed_col)

        if 0 <= aimed_row < 7 and 0 <= aimed_col < 7:
            hit_target = matrix[aimed_row][aimed_col]

            if hit_target.isdigit():
                hit_target = int(hit_target)
                players[player] = players[player] - hit_target
            elif hit_target == 'D':
                players[player] -= (corresponding_numbers(aimed_row, aimed_col, matrix) * 2)
            elif hit_target == 'T':
                players[player] -= (corresponding_numbers(aimed_row, aimed_col, matrix) * 3)
            elif hit_target == 'B':
                winner = True
                print(f'{player} won the game with {throws} throws!')
                break

            if players[player] <= 0:
                winner = True
                print(f'{player} won the game with {throws} throws!')
