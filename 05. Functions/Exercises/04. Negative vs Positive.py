numbers = [int(num) for num in input().split()]


def is_nonnegative(num):
    return num >= 0


positive = filter(is_nonnegative, numbers)
negative = filter(lambda num: num < 0, numbers)

positive_sum = sum(positive)
negative_sum = sum(negative)

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print(F"The positives are stronger than the negatives")
else:
    print(F"The negatives are stronger than the positives")