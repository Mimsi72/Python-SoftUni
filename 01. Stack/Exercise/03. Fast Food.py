from collections import deque
food_quantity = int(input())
order_queue = deque()
for order in input().split():
    order_queue.append(int(order))
print(max(order_queue))

for i in range(len(order_queue)):
    order = order_queue.popleft()
    if food_quantity >= order:
        food_quantity -= order
    else:
        order_queue.appendleft(order)
        print(f"Orders left: {(' '.join([str(order) for order in order_queue]))}")
        break

if len(order_queue) == 0:
    print("Orders complete")
