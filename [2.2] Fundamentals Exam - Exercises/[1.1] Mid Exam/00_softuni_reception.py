first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

total_employees = first_employee + second_employee + third_employee
hour_counter = 0

while students > 0:
    if hour_counter % 4 == 0:
        hour_counter += 1

    students -= total_employees

    if students <= 0:
        break

    hour_counter += 1

print(f"Time needed: {hour_counter}h.")
