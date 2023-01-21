start = int(input())
finish = int(input())
characters = ""
for i in range(start, finish + 1):
    characters = chr(i)
    print(characters, end=" ")
