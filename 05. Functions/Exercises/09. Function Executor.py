def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*funcs_with_args):
    res = []

    for func, frags in funcs_with_args:
        func_result = func(*frags)
        res.append(func_result)

    return res

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

