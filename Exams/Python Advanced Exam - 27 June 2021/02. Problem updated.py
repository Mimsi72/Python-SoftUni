def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def check_for_targets(matrix):
    targets = []
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == TARGET_SYMBOL:
                targets.append([i, j])
    return targets

matrix = []
player_position = None

for row in range(5):
    row_data = input().split()
    if "A" in row_data:
        player_position = [row, row_data.index("A")]
    matrix.append(row_data)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
EMPTY_SYMBOL = '.'
TARGET_SYMBOL = 'x'
PLAYER_SYMBOL = 'A'

n = int(input())
hit_targets = []
for _ in range(n):
    line = input().split()
    command = line[0]
    direction = line[1]
    if command == 'move':
        steps = int(line[2])
        (row, col) = player_position
        if direction == 'up':
            r, c = (row - steps), col
            if is_in_range((row - steps), col, 5):
                if matrix[r][c] == EMPTY_SYMBOL:
                    matrix[row][col] = EMPTY_SYMBOL
                    matrix[r][c] = PLAYER_SYMBOL
                    player_position = [r, c]
                else:
                    pass
        elif direction == 'down':
            r, c = (row + steps), col
            if is_in_range((row + steps), col, 5):
                if matrix[r][c] == EMPTY_SYMBOL:
                    matrix[row][col] = EMPTY_SYMBOL
                    matrix[r][c] = PLAYER_SYMBOL
                    player_position = [r, c]
                else:
                    pass
        elif direction == 'left':
            r, c = row, (col - steps)
            if is_in_range(row, (col - steps), 5):
                if matrix[r][c] == EMPTY_SYMBOL:
                    matrix[row][col] = EMPTY_SYMBOL
                    matrix[r][c] = PLAYER_SYMBOL
                    player_position = [r, c]
                else:
                    pass
        elif direction == 'right':
            r, c = row, (col + steps)
            if is_in_range(row, (col + steps), 5):
                if matrix[r][c] == EMPTY_SYMBOL:
                    matrix[row][col] = EMPTY_SYMBOL
                    matrix[r][c] = PLAYER_SYMBOL
                    player_position = [r, c]
                else:
                    pass
    if command == 'shoot':
        row, col = player_position
        for direct in directions:
            if direct == direction:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                while is_in_range(next_row, next_col, 5):
                    target = matrix[next_row][next_col]
                    if target == TARGET_SYMBOL:
                        hit_targets.append([next_row, next_col])
                        matrix[next_row][next_col] = EMPTY_SYMBOL
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if check_for_targets(matrix):
    print(f"Training not completed! {len(check_for_targets(matrix))} targets left.")
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
for i in hit_targets:
    print(i)
