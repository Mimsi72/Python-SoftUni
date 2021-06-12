words = input().split(' ')
output = (x for x in words if len(x) % 2 == 0)
print('\n'.join(output))
