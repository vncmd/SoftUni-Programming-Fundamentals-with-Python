def is_valid_length(password):
    return 6 <= len(password) <= 10


def is_alpha_numeric_ch(password):
    return password.isalnum()


def is_at_least_two_digit(password):
    digits = 0
    for ch in password:
        if ch.isdigit():
            digits += 1

    return digits >= 2


input_password = input()

is_valid = True

if not is_valid_length(input_password):
    is_valid = False
    print("Password must be between 6 and 10 characters")

if not is_alpha_numeric_ch(input_password):
    is_valid = False
    print("Password must consist only of letters and digits")

if not is_at_least_two_digit(input_password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")





# Different solution:

# def password_validation(passwrd):
#     validation = []
#
#     if len(passwrd) < 6 or len(passwrd) > 10:
#         validation.append("Password must be between 6 and 10 characters")
#     if not passwrd.isalnum():
#         validation.append("Password must consist only of letters and digits")
#
#     digit_counter = 0
#     for character in passwrd:
#         if character.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         validation.append("Password must have at least 2 digits")
#
#     return validation
#
#
# password = input()
# not_valid = password_validation(password)
#
# if len(not_valid) == 0:
#     print("Password is valid")
# else:
#     print('\n'.join(not_valid))