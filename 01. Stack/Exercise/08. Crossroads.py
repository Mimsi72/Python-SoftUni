green_light_duration = int(input())
free_window_duration = int(input())
is_crash = False
line = input()
stack = []
while line != "End":
    if is_crash:
        break
    if line == "green":
        for i in range(green_light_duration):
            stack.pop()
        if stack:
            pass # to be continued
    else:
        stack.append(line)
    line = input()
