n = int(input())

intersection_size = ()
for _ in range(n):
    first_line, second_line = input().split('-')

    first_line = first_line.split(',')
    second_line = second_line.split(',')

    first_line_start, first_line_end = int(first_line[0]), int(first_line[1])
    second_line_start, second_line_end = int(second_line[0]), int(second_line[1])

    first_line = set(range(first_line_start, first_line_end + 1))
    second_line = set(range(second_line_start, second_line_end + 1))

    current_intersection_size = first_line.intersection(second_line)

    if len(current_intersection_size) > len(intersection_size):
        intersection_size = current_intersection_size

intersection_size = list(intersection_size)
print(F"Longest intersection is {intersection_size} with length {len(intersection_size)}")
