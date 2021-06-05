n = int(input())

chemicals = set()

for _ in range(n):
    chemicals = chemicals.union(input().split())

for element in chemicals:
    print(element)