electrons = int(input())

result = []
while electrons > 0:
    n = len(result) + 1
    shell_value = min(2 * (n ** 2), electrons)
    result.append(shell_value)
    electrons -= shell_value

print(result)