key = int(input())
n_lines = int(input())

word = []
for i in range(n_lines):
    letter = input()
    check = ord(letter) + key
    word.append(chr(check))
for letter in word:
    print(letter, end="")