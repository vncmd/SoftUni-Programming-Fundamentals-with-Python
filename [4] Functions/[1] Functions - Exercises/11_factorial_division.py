def factorial(number):
    for current_num in range(1, number):
        number *= current_num
    return number


first = int(input())
second = int(input())

first_num_factorial = factorial(first)
second_num_factorial = factorial(second)

final_result = first_num_factorial / second_num_factorial
print(f"{result:.2f}")