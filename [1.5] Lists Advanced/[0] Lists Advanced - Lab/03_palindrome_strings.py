main_list = input().split(" ")

word_input = input()

find_word = []

for word in main_list:
    if word == word[::-1]:
        find_word.append(word)

print(f"{find_word}")
print(f"Found palindrome {find_word.count(word_input)} times")
