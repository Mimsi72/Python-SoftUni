def math_operations(*nums, **operations):
    counter = 1
    nums = list(nums)
    for num in nums:
        if counter == 1:
            operations["a"] += num
            counter += 1

        elif counter == 2:
            operations["s"] -= num
            counter += 1

        elif counter == 3:
            try:
                operations["d"] /= num
                counter += 1
            except ZeroDivisionError:
                counter += 1

        elif counter == 4:
            operations["m"] *= num
            counter = 1

    return operations

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
