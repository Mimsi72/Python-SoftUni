from collections import deque
children = deque(input().split())
count = int(input())

while len(children) > 1:
    children.rotate(-count)
    #Rotate with - left
    #without - right
    print(F"Removed {children.pop()}")

print(F"Last is {children.pop()}")
