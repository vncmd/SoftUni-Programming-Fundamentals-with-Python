count_students = int(input())

student_data = {}

for student in range(count_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in student_data:
        student_data[student_name] = []
    student_data[student_name].append(student_grade)

for student, grade in student_data.items():
    avg_grade = sum(grade) / len(grade)
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")