first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_questions = int(input())

total_employees = first_employee + second_employee + third_employee
hour_counter = 0

while students_questions > 0:
    if hour_counter % 4 == 0:
        hour_counter += 1

    students_questions -= total_employees

    if students_questions <= 0:
        break

    hour_counter += 1

print(f"Time needed: {hour_counter}h.")


# Different Solution:

# employee_info = [int(input()) for num in range(4)]
#
# answers_per_hr = sum(employee_info[:-1])
# students_questions = employee_info[-1]
# time_needed = 0
#
# while students_questions > 0:
#     time_needed += 1
#
#     if time_needed % 4 != 0:
#         students_questions -= answers_per_hr
#
# print(f"Time needed: {time_needed}h.")
