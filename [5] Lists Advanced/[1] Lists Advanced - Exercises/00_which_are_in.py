def is_sub_str(word, seq):
    for el in seq:
        found_sub_str = word in el
        if found_sub_str:
            return True

    return False


first = input().split(", ")
second = input().split(", ")

result = [x for x in first if is_sub_str(x, second)]

print(result)
