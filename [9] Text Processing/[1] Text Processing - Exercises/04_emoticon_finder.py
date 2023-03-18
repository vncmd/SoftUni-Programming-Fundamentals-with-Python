input_text = input()
for index in range(len(input_text)):

    if input_text[index] == ":":
        print(f":{input_text[index + 1]}")
