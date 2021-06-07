def is_even(num):
    return num % 2 == 0


numbers = [int(num) for num in (input().split())]
print(list(filter(is_even, numbers)))
