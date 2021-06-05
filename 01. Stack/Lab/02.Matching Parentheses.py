expression = input()
stack = []

for idx in range(len(expression)):
    if expression[idx] == "(":
        stack.append(idx)
    elif expression[idx] == ")":
        start_idx = stack.pop()
        print(expression[start_idx: idx+1])
