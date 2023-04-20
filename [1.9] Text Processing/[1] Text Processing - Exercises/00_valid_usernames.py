def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_chars(name):
    for character in name:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True


def redundant_symbols(name):
    if ' ' in name:
        return False
    return True


def user_validation(name):
    if valid_length(name) and valid_chars(name) and redundant_symbols(name):
        return True
    return False


input_username = input().split(", ")
for username in input_username:
    if user_validation(username):
        print(username)