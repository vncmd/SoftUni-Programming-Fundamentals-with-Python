def ban_user(name):
    ban_user_list.append(name)


def add_user(name, language, score):
    student_information[language] = student_information.get(language, {})
    student_information[language][name] = student_information[language].get(name, 0)
    student_information[language][submissions] = student_information[language].get(submissions, 0)
    if student_information[language][name] < score:
        student_information[language][name] = score
    student_information[language][submissions] += 1


def show_result():
    global submissions
    print("Results:")
    for key in student_information:
        for name, score in student_information[key].items():
            if all([name not in ban_user_list, submissions not in name]):
                print(f"{name} | {score}")
    print(f"{submissions}:")
    for key in student_information:
        if student_information[key]:
            print(f"{key} - {student_information[key][submissions]}")


user_command = input()
student_information = {}
ban_user_list = []
submissions = "Submissions"


while user_command != "exam finished":
    user_command = user_command.split("-")
    if user_command[-1] == "banned":
        ban_user(user_command[0])
    else:
        add_user(user_command[0], user_command[1], int(user_command[-1]))
    user_command = input()

show_result()
