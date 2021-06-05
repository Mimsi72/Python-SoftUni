from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(int(n) for n in input().split())
locks = deque(int(num) for num in input().split())
intelligence_value = int(input())
shots = 0
while bullets and locks:
    fires_bullets = bullets.pop()
    aimed_lock = locks.popleft()
    shots += 1
    if fires_bullets > aimed_lock:
        locks.appendleft(aimed_lock)
        print("Ping!")
    else:
        print("Bang!")
    if shots % gun_barrel_size == 0 and bullets:
        print("Reloading!")


bullets_cost = shots * bullet_price
earnings = intelligence_value - bullets_cost


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earnings}")
