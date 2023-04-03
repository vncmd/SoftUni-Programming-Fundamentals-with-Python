messages = int(input())

for i in range(messages):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print(f"GREAT!")
    else:
        print("Bye.")
