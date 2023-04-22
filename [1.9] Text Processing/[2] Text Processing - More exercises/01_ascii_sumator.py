start_char = input()
end_char = input()
string = input()

result = 0
for char in string:
    if ord(start_char) < ord(char) < ord(end_char):
        result += ord(char)

print(result)
