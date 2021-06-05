from collections import deque

robots = input().split(";")
robots_data = {}

for robot in robots:
    name, process_time = robot.split("-")
    process_time = int(process_time)
    robots_data[name] = {"process_time": process_time, "availability": True, "time_until_available": process_time}

hh, mm, ss = map(int, input().split(":"))

products = deque()
product = input()
while not product == "End":
    products.append(product)
    product = input()

while products:
    ss += 1
    if ss == 60:
        mm += 1
        ss = 0
    if mm == 60:
        hh += 1
        mm = 0
    if hh == 24:
        hh = 0

    working_robot = 0
    for robot in robots_data:
        if robots_data[robot]["availability"]:
            print(f"{robot} - {products.popleft()} [{hh:02d}:{mm:02d}:{ss:02d}]")
            robots_data[robot]["availability"] = False
        working_robot += 1
    if working_robot == len(robots_data):
        products.rotate(-1)

    for robot in robots_data:
        if not robots_data[robot]["availability"]:
            robots_data[robot]["time_until_available"] -= 1
            if robots_data[robot]["time_until_available"] == 0:
                robots_data[robot]["availability"] = True
                robots_data[robot]["time_until_available"] = robots_data[robot]["process_time"]