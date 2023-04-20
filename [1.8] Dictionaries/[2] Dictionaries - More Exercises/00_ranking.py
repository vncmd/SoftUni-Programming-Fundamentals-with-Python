add_people = input()

exams_information = {"contest": {}, "students": {}}
contest_dict = "contest"
students_dict = "students"

while add_people != "end of contests":

    add_people = add_people.split(":")
    contest = add_people[0]
    contest_pass = add_people[-1]
    exams_information[contest_dict][contest] = contest_pass
    add_people = input()

submissions = input()

while submissions != "end of submissions":

    submissions = submissions.split("=>")
    contest = submissions[0]
    contest_pass = submissions[1]
    contest_user = submissions[2]
    contest_points = int(submissions[-1])
    if contest in exams_information[contest_dict]:
        if exams_information[contest_dict][contest] == contest_pass:
            if contest_user not in exams_information[students_dict]:
                exams_information[students_dict][contest_user] = {}
            if contest not in exams_information[students_dict][contest_user]:
                exams_information[students_dict][contest_user][contest] = 0
            if exams_information[students_dict][contest_user][contest] < contest_points:
                exams_information[students_dict][contest_user][contest] = contest_points

    submissions = input()


def show_result():
    best_name = ""
    total_points = 0

    for name in exams_information[students_dict]:
        score_for_user = sum(exams_information[students_dict][name].values())
        if score_for_user > total_points:
            total_points = score_for_user
            best_name = name

    print(f"Best candidate is {best_name} with total {total_points} points.\nRanking:")

    for name in sorted(exams_information[students_dict]):
        print(name)

        for cur_contest, points in sorted(exams_information[students_dict][name].items(), key=lambda item: -item[1]):
            print(f"#  {cur_contest} -> {points}")


show_result()
