from collections import deque
pizza_orders = deque()
for order in input().split(', '):
    pizza_orders.append(int(order))

employees_capacities = input().split(',')
total_count = 0
while pizza_orders and employees_capacities:
    order = pizza_orders.popleft()
    if order <= 0 or order > 10:
        continue
    employee = int(employees_capacities.pop())

    if employee >= order:
        total_count += order
    else:
        order = order - employee
        total_count += employee
        pizza_orders.appendleft(order)


if len(pizza_orders) == 0:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {total_count}')
    print(f'Employees: {(",".join(str(employee) for employee in employees_capacities))}')
else:
    print('Not all orders are completed.')
    print(f"Orders left: {(', '.join([str(order) for order in pizza_orders]))}")
