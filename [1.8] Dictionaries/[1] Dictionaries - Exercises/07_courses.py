command = input()

course = {}
while command != "end":
    command = command.split(" : ")
    language_name = command[0]
    student = command[1]
    course[language_name] = course.get(language_name, {})
    course[language_name][student] = student
    command = input()

for language in course:
    print(f"{language}: {len(course[language])}")
    for key, value in course[language].items():
        print(f"-- {value}")
