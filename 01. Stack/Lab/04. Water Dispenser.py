from collections import deque
litters = int(input())
queue = deque()

name = input()
while not name == "Start":
    queue.append(name)
    name = input()

command = input()
while not command == "End":
    if command.startswith("refill"):
        litters += int(command.split()[-1])
    else:
        litters_wanted = int(command)
        name = queue.popleft()
        if litters_wanted <= litters:
            litters -= litters_wanted
            print(F"{name} got water")
        else:
            print(F"{name} must wait")
    command = input()
print(F"{litters} liters left")
