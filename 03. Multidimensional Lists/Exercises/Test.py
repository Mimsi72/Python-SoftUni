def read_bord():
    n = int(input())

    matrix = []
    for row in range(n):
        matrix.append([el for el in list(input())])
    return matrix


def knights_are_attacking(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'K':

                position_to_check = [
                    (row - 2, col + 1),
                    (row - 1, col + 2),
                    (row + 1, col + 2),
                    (row + 2, col + 1),
                    (row + 2, col - 1),
                    (row + 1, col - 2),
                    (row - 1, col - 2),
                    (row - 2, col - 1)
                ]
                for position in position_to_check:
                    pos_row, pos_col = position

                    if not (0 <= pos_row <= len(matrix) - 1):
                        continue
                    if not (0 <= pos_col <= len(matrix) - 1):
                        continue
                    if matrix[pos_row][pos_col] == 'K':
                        return True

    return False


def find_all_knights(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'K':
                positions.append((i, j))

    return positions


def calculate_aggression(matrix, knights_position):
    aggression_scores = {}
    for row, col in knights_position:

        position_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1)
        ]

        attacked_count = 0
        for attached_row, attacked_col in position_to_check:
            if not (0 <= attached_row <= len(matrix) - 1):
                continue
            if not (0 <= attacked_col <= len(matrix) - 1):
                continue
            if matrix[attached_row][attacked_col] == 'K':
                attacked_count += 1
        aggression_scores[(row, col)] = attacked_count
    return aggression_scores


def find_max_aggression(aggression_scores):
    max_so_far = None
    max_pos = None

    for pos, aggression in aggression_scores.items():
        if max_so_far is None or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos

    return max_pos


def main():
    matrix = read_bord()
    removed_knights = 0
    while knights_are_attacking(matrix) is True:
        knights_position = find_all_knights(matrix)
        aggression_scores = calculate_aggression(matrix, knights_position)
        row, col = find_max_aggression(aggression_scores)

        matrix[row][col] = '0'
        removed_knights += 1
    print(removed_knights)


main()
