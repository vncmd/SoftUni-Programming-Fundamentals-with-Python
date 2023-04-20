def check_palindrome(numbers):
    for nums in numbers:
        if nums == nums[::-1]:
            print("True")
        else:
            print("False")


input_nums = input().split(", ")
check_palindrome(input_nums)