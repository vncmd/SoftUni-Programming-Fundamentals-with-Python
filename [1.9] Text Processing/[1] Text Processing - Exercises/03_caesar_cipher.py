start_msg = input()
final_msg = ''

for chars in start_msg:
    new_symbol = chr(ord(chars) + 3)
    final_msg += new_symbol

print(final_msg)