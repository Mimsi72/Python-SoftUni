m, n = input().split()
m, n = int(m), int(n)

set_a, set_b = set(), set()

for _ in range(m):
    set_a.add(input())

for _ in range(n):
    set_b.add(input())

intersection = set_a & set_b
for el in intersection:
    print(el)
