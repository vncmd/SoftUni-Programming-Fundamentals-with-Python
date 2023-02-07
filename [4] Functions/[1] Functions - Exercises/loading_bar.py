def loading_bar(nums):
    num_range = int(nums / 10)
    target = 10
    if target == num_range:
        return "100% Complete!\n" + "[" + target * "%" + "]"
    else:
        return f"{nums}% " + "[" + num_range * "%" + (target - num_range) * "." + "]\n" + "Still loading..."


number = int(input())
print(loading_bar(number))