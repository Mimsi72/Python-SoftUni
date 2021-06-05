start, end = input().split(',')
start, end = int(start), int(end)
line_set = set()

current = start
while True:
    if current > end:
        break
    line_set.add(current)
    current = current+1
print(line_set)
print(type(line_set))
