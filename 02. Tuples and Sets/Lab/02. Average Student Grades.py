n = int(input())

student_grades = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in student_grades:
        student_grades[name] = grade
    elif not isinstance(student_grades[name], list):
        student_grades[name] = [student_grades[name]]
        student_grades[name].append(grade)


def calculate_avg(iter):
    return sum(iter) / len(iter)


for key, value in student_grades.items():
    avg = calculate_avg(student_grades[key])
    #for key in student_grades(key):
       # student_grades[key] = "{:.2f}".format(student_grades[key])
    print(f"{key} -> {value} (avg: {avg})")
