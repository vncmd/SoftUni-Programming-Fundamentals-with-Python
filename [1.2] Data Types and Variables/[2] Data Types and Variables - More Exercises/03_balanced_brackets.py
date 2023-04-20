number = int(input())
counter = 0
for iterations in range(number):
    check = input()
    if "(" in check:
        counter += 1
    elif ")" in check:
        counter -= 1
    if 0 != counter != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")