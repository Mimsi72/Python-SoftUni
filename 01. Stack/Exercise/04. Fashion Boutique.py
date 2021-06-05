box = ([int(x) for x in input().split()])
capacity = int(input())

current_capacity = 0
used_racks = 1

for i in range(len(box)):
    item = box.pop()

    if item + current_capacity <= capacity:
        current_capacity += item
    else:
        used_racks += 1
        current_capacity = item

print(used_racks)
