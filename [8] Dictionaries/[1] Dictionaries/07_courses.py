command = input()

course = {}
while command != "end":
    command = command.split(" : ")
    language_name = command[0]
    student = command[1]
    course[language_name] = course.get(language_name, {})
    course[language_name][student] = student
    command = input()

for lang in course:
    print(f"{lang}: {len(course[lang])}")
    for key, value in course[lang].items():
        print(f"-- {value}")

