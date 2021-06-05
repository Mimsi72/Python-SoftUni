parking_lot = int(input())
cars = set()


for _ in range(parking_lot):
    command, car_plate = input().split(', ')
    if command == 'IN':
        cars.add(car_plate)
    else:
        if car_plate in cars:
            cars.remove(car_plate)


if cars:
    print('\n'.join(cars))
else:
    print('Parking Lot is Empty')
