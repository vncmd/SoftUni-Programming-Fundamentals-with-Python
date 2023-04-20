def chars_range(start, end):
    result = []
    for num in range(ord(start) + 1, ord(end)):
        result.append(chr(num))

    return result


start_ch = input()
end_ch = input()

res_ch = chars_range(start_ch, end_ch)
print(" ".join(res_ch))