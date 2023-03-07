data = input()

courses = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name

    data = input()


course_name = data.replace("_", " ")
students = courses[course_name]

for student_id, name in students.items():
    print(f"{name} - {student_id}")