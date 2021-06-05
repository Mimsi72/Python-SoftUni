from collections import deque

queue = deque()
n = int(input())
for _ in range(n):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for i in range(n):
    tank_fuel = 0
    traveled_pumps = 0
    for gas_pump in queue:
        fuel, distance_to_next = gas_pump[0], gas_pump[1]
        tank_fuel += fuel
        if tank_fuel < distance_to_next:
            break

        tank_fuel -= distance_to_next
        traveled_pumps += 1
    if traveled_pumps == len(queue):
        print(i)
        break

    queue.rotate(-1)
