number_of_sequences = int(input())

for _ in range(number_of_sequences):
    first_line, second_line = input().split('-')
    first_line, second_line = set(first_line), set(second_line)


    def set_sequences(set_sequence):
        start, end = set_sequence().split(',')
        start, end = int(start), int(end)
        line_set = set()

        current = start
        while True:
            if current > end:
                break
            line_set.add(current)
            current = current + 1
        return line_set


    first_sequence = set_sequences(first_line())
    second_sequence = set_sequences(second_line())

    print(first_sequence)
    print(second_sequence)
