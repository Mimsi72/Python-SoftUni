num = int(input())
stack = []
for idx in range(num):
    line = input().split()
    command = line[0]
    if command == "1":
        stack.append(line[1])
    elif command == "2":
        if len(stack) > 0:
            stack.pop()
    elif command == "3":
        if len(stack) > 0:
            print(max(stack))
    else:
        if len(stack) > 0:
            print(min(stack))

stack_reversed = []
for i in range(len(stack)):
    stack_reversed.append(stack.pop())

print(", ".join(stack_reversed))
print(type(stack_reversed))
