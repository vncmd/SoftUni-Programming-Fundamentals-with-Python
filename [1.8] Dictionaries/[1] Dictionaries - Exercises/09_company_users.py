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


# Different solution:

# def employee_id_search(id):
#     for value in company_db[id].values():
#         if id == value:
#             return True
#     return False
#
#
# command = input()
# company_db = {}
#
# while command != "End":
#     company_name, employee_id = command.split(" -> ")
#
#     company_db[company_name] = company_db.get(company_name, {})
#
#     if not employee_id_search(company_name):
#         company_db[company_name][employee_id] = employee_id
#
#     command = input()
#
# for employee in company_db:
#     print(employee)
#
#     for key, value in company_db[employee].items():
#         print(f"-- {value}")
