text = input()

result = [char for char in text if char.lower() not in ["a", "o", "e", "i"]]

print("".join(result))