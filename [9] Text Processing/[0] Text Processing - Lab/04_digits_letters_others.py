text = input()

letters = ""
digits = ""
symbols = ""

for char in text:

    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)