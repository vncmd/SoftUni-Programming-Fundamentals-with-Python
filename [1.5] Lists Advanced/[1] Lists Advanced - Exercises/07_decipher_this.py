message = input().split()

words = []
numbers = []
for word in message:
    nums = ""
    letter = ""
    for symbol in word:
        if symbol.isdigit():
            nums += symbol
        else:
            letter += symbol
    numbers.append(int(nums))
    if len(letter) != 1:
        letter = f"{letter[-1]}{letter[1:-1]}{letter[0]}"
    words.append(letter)

for num, wrd in zip(numbers, words):
    print(f"{chr(num)}{wrd}", end=" ")