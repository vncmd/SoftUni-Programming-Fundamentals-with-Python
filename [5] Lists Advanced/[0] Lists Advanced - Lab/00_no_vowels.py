text = input()
vowels = ["a", "o", "u", "e", "i"]
result = [char for char in text if char.lower() not in vowels]

print("".join(result))