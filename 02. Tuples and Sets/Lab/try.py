n = int(input())

student_grades = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in student_grades:
        student_grades[name] = grade
    else:
        student_grades[name].append(grade)

print(f"{''.join(student_grades)}")
