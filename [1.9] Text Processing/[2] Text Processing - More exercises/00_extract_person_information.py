num_lines = int(input())

for _ in range(num_lines):
    person_id = input()
    name = person_id[person_id.index("@") + 1:person_id.index("|")]
    age = person_id[person_id.index("#") + 1:person_id.index("*")]

    print(f"{name} is {age} years old.")