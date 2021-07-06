from collections import deque

chocolates = deque([el for el in input().split(", ")])
cup_of_milk = deque([el for el in input().split(", ")])

milkshades = 0
is_Ready = False

while chocolates and cup_of_milk:
    chocolate_mix = chocolates.pop()
    milk_mix = cup_of_milk.popleft()
    chocolate_mix = int(chocolate_mix)
    milk_mix = int(milk_mix)
    if chocolate_mix <= 0 and milk_mix <= 0:
        continue
    if chocolate_mix <= 0:
        cup_of_milk.appendleft(str(milk_mix))
        continue
    elif milk_mix <= 0:
        chocolates.append(str(chocolate_mix))
        continue
    elif chocolate_mix == milk_mix:
        milkshades += 1
    elif chocolate_mix != milk_mix:
        cup_of_milk.append(str(milk_mix))
        chocolate_mix -= 5
        chocolates.append(str(chocolate_mix))

    if milkshades >= 5:
        is_Ready = True
        break

if is_Ready:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")
if cup_of_milk:
    print(f"Milk: {', '.join(cup_of_milk)}")
else:
    print("Milk: empty")
