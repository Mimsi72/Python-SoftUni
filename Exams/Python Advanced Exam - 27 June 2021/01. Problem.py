from collections import deque

chocolates = deque([int(el) for el in input().split(", ")])
cups_of_milk = deque([int(el) for el in input().split(", ")])
milkshakes = 0

while chocolates and cups_of_milk:
    chocolate_mix = chocolates.pop()
    milk_mix = cups_of_milk.popleft()
    if milk_mix <= 0:
        chocolates.append(chocolate_mix)
        continue
    if chocolate_mix <= 0:
        cups_of_milk.appendleft(milk_mix)
        continue
    if milk_mix == chocolate_mix:
        milkshakes += 1
    else:
        chocolate_mix -= 5
        chocolates.append(chocolate_mix)
        cups_of_milk.append(milk_mix)
    if milkshakes >= 5:
        print(f'Great! You made all the chocolate milkshakes needed!')
        if not chocolates:
            print(f"Chocolate: empty")
        else:
            print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
        if cups_of_milk:
            print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
        else:
            print("Milk: empty")
        break

if milkshakes < 5:
    print("Not enough milkshakes.")
    if not chocolates:
        print(f"Chocolate: empty")
    else:
        print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
    if cups_of_milk:
        print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
    else:
        print("Milk: empty")
