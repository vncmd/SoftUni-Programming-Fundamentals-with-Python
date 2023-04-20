command = input()
num = input()


def action(data_type, value):
    if data_type == "int":
        result = float(value) * 2
        return f"{result:.0f}"

    elif data_type == "real":
        result = float(value) * 1.5
        return f"{result:.2f}"

    elif data_type == "string":
        return f"${value}$"


print(action(command, num))
