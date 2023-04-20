command = input()
company_data = {}

while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in company_data:
        company_data[company] = []
    if employee_id not in company_data[company]:
        company_data[company].append(employee_id)
    command = input()

for current_company in company_data.items():
    company_name = current_company[0]
    print(company_name)
    employees = current_company[1]
    for employee in range(len(employees)):
        print(f"-- {employees[employee]}")
